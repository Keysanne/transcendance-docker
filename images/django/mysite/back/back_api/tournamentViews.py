from django.shortcuts import render
from .models import User, Tournament, Contestant
from rest_framework import generics
from .serializers import UserSerializer, TournamentSerializer, ContestantSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def tournamentList(request):
	queryset = Tournament.objects.all().filter(status=0)
	serializer = TournamentSerializer(queryset, many=True)

	lst = []
	for t in serializer.data:
		contestants = list(Contestant.objects.all().filter(tournament=t['pk']))
		listofcontestants = []
		for c in contestants:
			dico = ContestantSerializer(c).data
			query = User.objects.get(pk=dico['user'])
			dico['username'] = query.username
			dico['pfp'] = UserSerializer(query, context={'request': request}, many=False).data['pfp']
			listofcontestants.append(dico)
		listofcontestants = sorted(listofcontestants, key=lambda x: x['position'])
		unit = {'pk': t['pk'], 'name':t['name'], 'description':t['description'], 'capacity': t['capacity'], 'organizer': t['organizer'], 'contestants':listofcontestants}
		lst.append(unit)
	return Response({'tournaments':lst}, status=status.HTTP_200_OK)


@api_view(['GET'])
def contestantList(request, tpk):
	try:
		Tournament.objects.get(pk=tpk)
	except:
		return Response({'problem': 'tournament does not exist'}, status=status.HTTP_400_BAD_REQUEST)

	try:
		contestants = Contestant.objects.all().filter(tournament=tpk)
		listofcontestants = []
		for c in contestants:
			dico = ContestantSerializer(c).data
			query = User.objects.get(pk=dico['user'])
			dico['username'] = query.username
			dico['pfp'] = UserSerializer(query, context={'request': request}, many=False).data['pfp']
			listofcontestants.append(dico)
		return Response({'contestants': listofcontestants}, status=status.HTTP_200_OK)
	except:
		return Response({'problem': 'problem while getting the contestants'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def tournamentStart(request, pk):
	try:
		queryset = Tournament.objects.get(pk=pk)
		if queryset.status != 1:
			return Response({'problem': 'tournament has already been started'}, status=status.HTTP_412_PRECONDITION_FAILED)
		if queryset.status != 2:
			return Response({'problem': 'tournament has already finished'}, status=status.HTTP_412_PRECONDITION_FAILED)

		contestants = Contestant.objects.all().filter(tournament=pk)
		if (len(contestants) != queryset.capacity):
			return Response({'problem': f'contestants: {len(contestants)}/{queryset.capacity}'}, status=status.HTTP_412_PRECONDITION_FAILED)

		queryset.status = 1
		queryset.save()
		return Response(status=status.HTTP_200_OK)
	except:
		return Response({'problem': 'tournament does not exist'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def addContestant(request, tpk, upk):
	try:
		User.objects.get(pk=upk)
	except:
		return Response({'problem': 'user does not exist'}, status=status.HTTP_400_BAD_REQUEST)
	try:
		tournament = Tournament.objects.get(pk=tpk)
	except:
		return Response({'problem': 'tournament does not exist'}, status=status.HTTP_400_BAD_REQUEST)

	try:
		if len(Contestant.objects.all().filter(tournament=tpk, user=upk)) != 0:
			return Response({'problem': 'user already registered'}, status=status.HTTP_409_CONFLICT)
	except:
		pass

	contestants = Contestant.objects.all().filter(tournament=tpk)
	if len(contestants) == tournament.capacity:
		return Response({'problem': 'tournament if full'}, status=status.HTTP_400_BAD_REQUEST)

	data = (str(request))[(str(request)).index('?') + 1:-2]
	data = data.split("&")
	for i in range (len(data)):
		data[i] = (data[i]).split("=")
	new_data = []
	for lst in data:
		for s in lst:
			new_data.append(s)
	data = {new_data[i]: new_data[i + 1] for i in range (0, len(new_data), 2)}

	data['tournament'] = tpk
	data['user'] = upk
	data['position'] = 0

	positions = []
	for i, c in enumerate(contestants):
		if positions == [] and c.position == 0:
			positions.append(c.position)
			data['position'] += 1
			continue
		elif positions == [] and c.position != 0:
			data['position'] = 0
			break
		elif c.position != positions[-1] + 1:
			data['position'] = positions[-1] + 1
			break
		else:
			positions.append(c.position)
			data['position'] += 1

	print (data['position'])

	serializer = ContestantSerializer(data=data)
	if serializer.is_valid():
		serializer.save()
		return Response(status=status.HTTP_201_CREATED)
	return Response({'problem': serializers.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def removeContestant(request, tpk, upk):
	try:
		tournament = Tournament.objects.get(pk=tpk)
		if tournament.status != 0:
			return Response({'problem': 'tournament cannot be quit'}, status=status.HTTP_412_PRECONDITION_FAILED)
	except:
		return Response({'problem': 'tournament does not exist'}, status=status.HTTP_400_BAD_REQUEST)

	try:
		User.objects.get(pk=upk)
	except:
		return Response({'problem': 'user does not exist'}, status=status.HTTP_400_BAD_REQUEST)

	try:
		Contestant.objects.all().filter(tournament=tpk, user=upk).delete()
		return Reponse(status=status.HTTP_200_OK)
	except:
		return Response({'problem': 'user is not a contestant'}, status=status.HTTP_412_PRECONDITION_FAILED)


@api_view(['PATCH'])
def userReady(request, tpk, upk):
	try:
		tournament = Tournament.objects.get(pk=tpk)
		if tournament.status != 1:
			return Response({'problem': 'tournament is not in the good status'}, status=status.HTTP_412_PRECONDITION_FAILED)
	except:
		return Response({'problem': 'tournament does not exist'}, status=status.HTTP_400_BAD_REQUEST)

	try:
		User.objects.get(pk=upk)
	except:
		return Response({'problem': 'user does not exist'}, status=status.HTTP_400_BAD_REQUEST)

	try:
		c = Contestant.objects.get(tournament=tpk, user=upk)
		if c.status == 0:
			return Response({'problem': 'contestant is dead'}, status=status.HTTP_412_PRECONDITION_FAILED)
		if c.status == 3:
			return Response({'problem': 'contestant is in game'}, status=status.HTTP_412_PRECONDITION_FAILED)
		if c.status == 2:
			return Response({'problem': 'contestant is already ready'}, status=status.HTTP_412_PRECONDITION_FAILED)
		if c.status == 1:
			c.status = 2
			c.save()
			return Response({'status': 'ready'}, status=status.HTTP_200_OK)

	except:
		return Response({'problem': 'contestant does not exist'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def matchStart(request, tpk):
	try:
		Tournament.objects.get(pk=tpk)
	except:
		return Response({'problem': 'tournament does not exist'}, status=status.HTTP_400_BAD_REQUEST)

	data = (str(request))[(str(request)).index('?') + 1:-2]
	data = data.split("&")
	for i in range (len(data)):
		data[i] = (data[i]).split("=")
	new_data = []
	for lst in data:
		for s in lst:
			new_data.append(s)
	data = {new_data[i]: int(new_data[i + 1]) for i in range (0, len(new_data), 2)}

	try:
		User.objects.get(pk=data['player1'])
	except:
		return Response({'problem': 'player1 does not exist'}, status=status.HTTP_400_BAD_REQUEST)
	try:
		User.objects.get(pk=data['player2'])
	except:
		return Response({'problem': 'player2 does not exist'}, status=status.HTTP_400_BAD_REQUEST)

	try:
		c1 = Contestant.objects.all().filter(tournament=tpk, user=data['player1'])
		if c1.status == 0:
			return Response({'problem': 'player1 is not alive'}, status=status.HTTP_412_PRECONDITION_FAILED)
		if c1.status != 2:
			return Response({'problem': 'player1 is not ready'}, status=status.HTTP_412_PRECONDITION_FAILED)
	except:
		return Response({'problem': 'player1 is not a contestant'}, status=status.HTTP_412_PRECONDITION_FAILED)
	try:
		c2 = Contestant.objects.all().filter(tournament=tpk, user=data['player2'])
		if c2.status == 0:
			return Response({'problem': 'player2 is not alive'}, status=status.HTTP_412_PRECONDITION_FAILED)
		if c2.status != 2:
			return Response({'problem': 'player2 is not ready'}, status=status.HTTP_412_PRECONDITION_FAILED)
	except:
		return Response({'problem': 'player2 is not a contestant'}, status=status.HTTP_412_PRECONDITION_FAILED)

	if (c1.position // (2**(c1.stage + 1))) != (c2.position // (2**(c2.stage + 1))):
		return Response({'problem': 'player1 and player2 cannot match'}, status=status.HTTP_412_PRECONDITION_FAILED)

	c1.status = 3
	c2.status = 3
	c1.save()
	c2.save()
	return Response(status=status.HTTP_200_OK)

@api_view(['PATCH'])
def tournamentMatchResult(request, tpk):
	try:
		tournament = Tournament.objects.get(pk=tpk)
		if tournament.status == 0:
			return Response({'problem': 'tournament hasn\'t started yet'}, status=status.HTTP_412_PRECONDITION_FAILED)
		if tournament.status == 2:
			return Response({'problem': 'tournament is already finished'}, status=status.HTTP_412_PRECONDITION_FAILED)
	except:
		return Response({'problem': 'tournament does not exist'}, status=status.HTTP_400_BAD_REQUEST)

	if not '?' in request:
		return Response({'problem': 'no data sent'})

	data = (str(request))[(str(request)).index('?') + 1:-2]
	data = data.split("&")
	for i in range (len(data)):
		data[i] = (data[i]).split("=")
	new_data = []
	for lst in data:
		for s in lst:
			new_data.append(s)
	data = {new_data[i]: int(new_data[i + 1]) for i in range (0, len(new_data), 2)}

	for info in ['player1', 'player2', 'player1score', 'player2score']:
		if info not in data.keys:
			return Response({'problem': 'lacking informations'}, status=status.HTTP_400_BAD_REQUEST)

	try:
		User.objects.get(pk=data['player1'])
	except:
		return Response({'problem': 'player1 does not exist'}, status=status.HTTP_400_BAD_REQUEST)
	try:
		User.objects.get(pk=data['player2'])
	except:
		return Response({'problem': 'player2 does not exist'}, status=status.HTTP_400_BAD_REQUEST)

	try:
		c1 = Contestant.objects.all().filter(tournament=tpk, user=data['player1'])
		if c1.status == 0:
			return Response({'problem': 'player1 is not alive'}, status=status.HTTP_412_PRECONDITION_FAILED)
		if c1.status != 3:
			return Response({'problem': 'player1 was not in game'}, status=status.HTTP_412_PRECONDITION_FAILED)
	except:
		return Response({'problem': 'player1 is not a contestant'}, status=status.HTTP_412_PRECONDITION_FAILED)
	try:
		c2 = Contestant.objects.all().filter(tournament=tpk, user=data['player2'])
		if c2.status == 0:
			return Response({'problem': 'player2 is not alive'}, status=status.HTTP_412_PRECONDITION_FAILED)
		if c2.status != 3:
			return Response({'problem': 'player2 was not in game'}, status=status.HTTP_412_PRECONDITION_FAILED)
	except:
		return Response({'problem': 'player2 is not a contestant'}, status=status.HTTP_412_PRECONDITION_FAILED)

	if (data['player1score'] > data['player2score']):
		c2.status = 0
		c2.status = 1
		c1.stage += 1
		diff = data['player1score'] - data['player2score']
		c1.score += 10 + diff
		c2.score -= 10 + diff
		c1.save()
		c2.save()
		return Response(status=status.HTTP_200_OK)
	if (data['player2score'] > data['player1score']):
		c1.status = 0
		c1.status = 1
		c2.stage += 1
		diff = data['player2score'] - data['player1score']
		c2.score += 10 + diff
		c1.score -= 10 + diff
		c1.save()
		c2.save()
		return Response(status=status.HTTP_200_OK)
	return Response({'problem': 'a tie is not possible'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def tournamentEnd(request, tpk):
	try:
		tournament = Tournament.objects.get(pk=tpk)
		if (tournament.status == 0):
			return Response({'problem': 'tournament hasn\'t started yet'}, status=status.HTTP_412_PRECONDITION_FAILED)
		if (tournament.status == 2):
			return Response({'problem': 'tournament has already ended'}, status=status.HTTP_412_PRECONDITION_FAILED)
	except:
		return Response({'problem': 'tournament does not exist'}, status=status.HTTP_400_BAD_REQUEST)

	try:
		contestants = Contestant.objects.all().filter(tournament=tpk, status=1)
		if (len(contestants) > 1):
			return Response({'problem': 'to many contestants alive'}, status=status.HTTP_412_PRECONDITION_FAILED)
		if (len(contestants) < 1):
			return Response({'problem': 'to few contestants alive'}, status=status.HTTP_412_PRECONDITION_FAILED)
		tournament.status = 2
		tournament.save()
	except:
		return Response({'problem': 'problem while obtaining the contestants'})
