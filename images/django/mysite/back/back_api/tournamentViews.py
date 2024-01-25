from django.shortcuts import render
from .models import User, Tournament, Contestant
from rest_framework import generics
from .serializers import UserSerializer, TournamentSerializer, ContestantSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
import sys


@api_view(['GET'])
@permission_classes([IsAuthenticated])
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
		unit = {'pk': t['pk'], 'name':t['name'], 'description':t['description'], 'status':t['status'], 'capacity': t['capacity'], 'organizer': t['organizer'], 'contestants':listofcontestants}
		lst.append(unit)

	queryset = Tournament.objects.all().filter(status=1)
	serializer = TournamentSerializer(queryset, many=True)

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
		unit = {'pk': t['pk'], 'name':t['name'], 'description':t['description'], 'status':t['status'], 'capacity': t['capacity'], 'organizer': t['organizer'], 'contestants':listofcontestants}
		lst.append(unit)
	return Response({'tournaments':lst}, status=status.HTTP_200_OK, headers={'Access-Control-Allow-Origin':'*'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def contestantList(request, tpk):
	try:
		queryset = Tournament.objects.get(pk=tpk)
		serializer = TournamentSerializer(queryset, many=False)
		t = serializer.data
	except:
		return Response({'problem': 'tournament does not exist'}, status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin':'*'})

	try:
		contestants = Contestant.objects.all().filter(tournament=tpk)
		listofcontestants = []
		for c in contestants:
			dico = ContestantSerializer(c).data
			query = User.objects.get(pk=dico['user'])
			dico['username'] = query.username
			dico['pfp'] = UserSerializer(query, context={'request': request}, many=False).data['pfp']
			listofcontestants.append(dico)
		return Response({'name': t["name"], 'description': t["description"], 'organizer': t["organizer"], 'contestants': listofcontestants}, status=status.HTTP_200_OK, headers={'Access-Control-Allow-Origin':'*'})
	except:
		return Response({'problem': 'problem while getting the contestants'}, status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin':'*'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def tournamentStart(request, pk):
	try:
		queryset = Tournament.objects.get(pk=pk)
		if queryset.status == 1:
			return Response({'problem': 'tournament has already been started'}, status=status.HTTP_412_PRECONDITION_FAILED, headers={'Access-Control-Allow-Origin':'*'})
		if queryset.status == 2:
			return Response({'problem': 'tournament has already finished'}, status=status.HTTP_412_PRECONDITION_FAILED, headers={'Access-Control-Allow-Origin':'*'})

		contestants = Contestant.objects.all().filter(tournament=pk)
		if (len(contestants) != queryset.capacity):
			return Response({'problem': f'contestants: {len(contestants)}/{queryset.capacity}'}, status=status.HTTP_412_PRECONDITION_FAILED, headers={'Access-Control-Allow-Origin':'*'})

		queryset.status = 1
		queryset.save()
		return Response(status=status.HTTP_200_OK, headers={'Access-Control-Allow-Origin':'*'})
	except:
		return Response({'problem': 'tournament does not exist'}, status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin':'*'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def addContestant(request, tpk, upk):
	try:
		User.objects.get(pk=upk)
	except:
		return Response({'problem': 'user does not exist'}, status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin':'*'})
	try:
		tournament = Tournament.objects.get(pk=tpk)
	except:
		return Response({'problem': 'tournament does not exist'}, status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin':'*'})

	try:
		if len(Contestant.objects.all().filter(tournament=tpk, user=upk)) != 0:
			return Response({'problem': 'user already registered'}, status=status.HTTP_409_CONFLICT, headers={'Access-Control-Allow-Origin':'*'})
	except:
		pass

	contestants = Contestant.objects.all().filter(tournament=tpk)
	if len(contestants) == tournament.capacity:
		return Response({'problem': 'tournament if full'}, status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin':'*'})

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

	for c in contestants:
		if c.nickname == data['nickname']:
			return Response({'problem': 'Nickname alrady used'}, status=status.HTTP_409_CONFLICT, headers={'Access-Control-Allow-Origin':'*'})

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
		return Response(status=status.HTTP_201_CREATED, headers={'Access-Control-Allow-Origin':'*'})
	return Response({'problem': serializers.errors}, status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin':'*'})


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def removeContestant(request, tpk, upk):
	try:
		tournament = Tournament.objects.get(pk=tpk)
		if tournament.status != 0:
			return Response({'problem': 'tournament cannot be quit'}, status=status.HTTP_412_PRECONDITION_FAILED, headers={'Access-Control-Allow-Origin':'*'})
	except:
		return Response({'problem': 'tournament does not exist'}, status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin':'*'})

	try:
		User.objects.get(pk=upk)
	except:
		return Response({'problem': 'user does not exist'}, status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin':'*'})

	try:
		Contestant.objects.all().filter(tournament=tpk, user=upk).delete()
		return Response(status=status.HTTP_200_OK, headers={'Access-Control-Allow-Origin':'*'})
	except:
		return Response({'problem': 'user is not a contestant'}, status=status.HTTP_412_PRECONDITION_FAILED, headers={'Access-Control-Allow-Origin':'*'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def tournamentEnd(request, tpk):
	try:
		tournament = Tournament.objects.get(pk=tpk)
		if (tournament.status == 0):
			return Response({'problem': 'tournament hasn\'t started yet'}, status=status.HTTP_412_PRECONDITION_FAILED, headers={'Access-Control-Allow-Origin':'*'})
		if (tournament.status == 2):
			return Response({'problem': 'tournament has already ended'}, status=status.HTTP_412_PRECONDITION_FAILED, headers={'Access-Control-Allow-Origin':'*'})
	except:
		return Response({'problem': 'tournament does not exist'}, status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin':'*'})

	try:
		contestants = Contestant.objects.all().filter(tournament=tpk, status=1)
		if (len(contestants) > 1):
			return Response({'problem': 'to many contestants alive'}, status=status.HTTP_412_PRECONDITION_FAILED, headers={'Access-Control-Allow-Origin':'*'})
		if (len(contestants) < 1):
			return Response({'problem': 'to few contestants alive'}, status=status.HTTP_412_PRECONDITION_FAILED, headers={'Access-Control-Allow-Origin':'*'})
		tournament.status = 2
		tournament.save()
	except:
		return Response({'problem': 'problem while obtaining the contestants'}, status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin':'*'})
