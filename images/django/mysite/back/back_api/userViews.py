from django.shortcuts import render
from .models import User, Tournament
from rest_framework import generics
from .serializers import UserSerializer, TournamentSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import authenticate
from PIL import Image
import jwt
import sys
from datetime import datetime
import django



@api_view(['POST'])
def UserCreate(request):
	data = (str(request))[(str(request)).index('?') + 1:-2]
	data = data.split("&")
	for i in range (len(data)):
		data[i] = (data[i]).split("=")
	new_data = []
	for lst in data:
		for s in lst:
			new_data.append(s)
	data = {new_data[i]: new_data[i + 1] for i in range (0, len(new_data), 2)}
	password_unhashed = data['password']
	data['password'] = make_password(data['password'])
	serializer = UserSerializer(data=data)
	try:
		queryset = User.objects.get(username=data['username'])
		return Response(status=status.HTTP_409_CONFLICT, headers={'Access-Control-Allow-Origin':'*'})
	except:
		if (serializer.is_valid()):
			serializer.save()
			username = data['username']
			password = password_unhashed
			user = authenticate(username=username, password=password)
			if user is not None:
				return Response({'pk':serializer.data['pk']}, status=status.HTTP_201_CREATED, headers={'Access-Control-Allow-Origin':'*'})
			else:
				return Response({'problem': 'JWT'}, status=status.HTTP_400_BAD_REQUEST)
	return Response({'problem':serializer.errors}, status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin':'*'})


@api_view(['GET'])
def UserConnect(request):
	data = (str(request))[(str(request)).index('?') + 1:-2]
	data = data.split("&")
	for i in range (len(data)):
		data[i] = (data[i]).split("=")
	new_data = []
	for lst in data:
		for s in lst:
			new_data.append(s)
	data = {new_data[i]: new_data[i + 1] for i in range (0, len(new_data), 2)}

	try:
		queryset = User.objects.get(username=data['username'])
	except:
		return Response({'problem': "username"}, status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin':'*'})
	if (check_password(data['password'], queryset.password) == True):
		username = data['username']
		password = data['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			return Response({'pk': queryset.pk}, status=status.HTTP_200_OK, headers={'Access-Control-Allow-Origin':'*'})
		else:
			return Response({'problem': 'JWT'}, status=status.HTTP_400_BAD_REQUEST)
	return Response({'problem': 'password'}, status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin':'*'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def UserList(request):
	queryset = User.objects.all()
	serializer = UserSerializer(queryset, context={'request': request}, many=True)

	leaderboard = sorted(serializer.data, key=lambda x: x['elo'], reverse=True)

	return Response([{'pk': u['pk'], 'username':u['username'], 'pfp':u['pfp'], 'elo':u['elo']} for i, u in enumerate(leaderboard)], headers={'Access-Control-Allow-Origin':'*'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def UserDetail(request, pk):
	try:
		queryset = User.objects.get(pk=pk)
		serializer = UserSerializer(queryset, context={'request': request}, many=False)

		ldb_query = User.objects.all()
		ldb_serial = UserSerializer(ldb_query, many=True)
		ldb_dict = sorted(ldb_serial.data, key=lambda x: x['elo'], reverse=True)

		for i, item in enumerate(ldb_dict):
			if (item['pk'] == pk):
				rank = i + 1
				break

		if (rank < queryset.best_rank):
			queryset.best_rank = rank
			queryset.save()

		return Response({'pk': queryset.pk, 'username': queryset.username, 'pfp':serializer.data['pfp'], 'wins': queryset.wins, 'losses': queryset.losses, 'elo':queryset.elo, 'best_elo':queryset.best_elo, 'rank': rank, 'best_rank': queryset.best_rank, 'language':queryset.language}, headers={'Access-Control-Allow-Origin':'*'})
	except:
		return Response({'pk':pk}, status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin':'*'})


@api_view(['PATCH', 'POST'])
@permission_classes([IsAuthenticated])
def UserUpdate(request, pk):
	if ("?" in str(request)):
		data = (str(request))[(str(request)).index('?') + 1:-2]
		data = data.split("&")
		for i in range (len(data)):
			data[i] = (data[i]).split("=")
		new_data = []
		for lst in data:
			for s in lst:
				new_data.append(s)
		data = {new_data[i]: new_data[i + 1] for i in range (0, len(new_data), 2)}

	try:
		queryset = User.objects.get(pk=pk)
		# serializer = UserSerializer(queryset, many=False)


		if '?' in str(request):
			keys = data.keys()
			queryset.password = make_password(data['password'])
			queryset.save()
		else :
			queryset.pfp = request.data['image_upload']
			queryset.save()

			if (queryset.pfp.width != queryset.pfp.height):
				img = Image.open(queryset.pfp.path)
				size = list(img.size)
				wi = int(size[0])
				he = int(size[1])

				if (he < wi):
					left = (wi - he) / 2
					right = wi - ((wi - he) / 2)
					top = 0
					bottom = he
				else:
					left = 0
					right = wi
					top = (he - wi) / 2
					bottom = he - ((he - wi) / 2)

				img = img.crop((left, top, right, bottom))
				img.save(queryset.pfp.path)

			queryset.save()

		return Response({'pk':pk}, status=status.HTTP_200_OK, headers={'Access-Control-Allow-Origin':'*'})

	except:
		return Response(status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin':'*'})


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def UserDelete(request, pk):
	try:
		queryset = User.objects.get(pk=pk).delete()
		return Response(status=status.HTTP_200_OK, headers={'Access-Control-Allow-Origin':'*'})
	except:
		return Response(status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin':'*'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createTournament(request, pk):

	data = (str(request))[(str(request)).index('?') + 1:-2]
	data = data.split("&")
	for i in range (len(data)):
		data[i] = (data[i]).split("=")
	new_data = []
	for lst in data:
		for s in lst:
			new_data.append(s)
	data = {new_data[i]: new_data[i + 1] for i in range (0, len(new_data), 2)}

	try:
		queryset = User.objects.get(pk=pk)
	except:
		return Response({'problem': 'user does not exist'}, status=status.HTTP_400_BAD_REQUEST)

	data['organizer'] = pk

	serializer = TournamentSerializer(data=data)

	if serializer.is_valid():
		serializer.save()
		return Response(status=status.HTTP_201_CREATED)
	return Response({'problem': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

