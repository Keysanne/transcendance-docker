from django.shortcuts import render
from .models import User, Tournament, Game
from rest_framework import generics
from .serializers import UserSerializer, TournamentSerializer, GameSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password, make_password
from datetime import datetime
from PIL import Image
import django
import sys
import os
import json
import requests

from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REMOTE_PASSWORD = os.getenv('REMOTE_PASSWORD')
ACCESS_TOKEN = response = requests.post(
		"https://api.intra.42.fr/oauth/token",
        data={"grant_type": "client_credentials"},
        auth=(CLIENT_ID, CLIENT_SECRET),
    ).json()["access_token"]


# def get_access_token():
#     response = requests.post(
#         "https://api.intra.42.fr/oauth/token",
#         data={"grant_type": "client_credentials"},
#         auth=(CLIENT_ID, CLIENT_SECRET),
#     )
#     return response.json()["access_token"]

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
	data['password'] = make_password(data['password'])
	serializer = UserSerializer(data=data)

	params = {'access_token': ACCESS_TOKEN}
	response = requests.get(f'https://api.intra.42.fr/v2/users?filter[login]={data["username"]}', params=params)
	if len(response.json()) != 0:
		return Response({'problem': 'username is 42 login'}, status=status.HTTP_409_CONFLICT)

	try:
		queryset = User.objects.get(username=data['username'])
		return Response(status=status.HTTP_409_CONFLICT, headers={'Access-Control-Allow-Origin':'*'})
	except:
		if (serializer.is_valid()):
			serializer.save()
			return Response({'pk':serializer.data['id']}, status=status.HTTP_201_CREATED, headers={'Access-Control-Allow-Origin':'*'})
		return Response({'problem':serializer.errors}, status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin':'*'})


@api_view(['GET', 'POST'])
def RemoteLogin(request):
	data = (str(request))[(str(request)).index('?') + 1:-2]
	data = data.split("&")
	for i in range (len(data)):
		data[i] = (data[i]).split("=")
	new_data = []
	for lst in data:
		for s in lst:
			new_data.append(s)
	data = {new_data[i]: new_data[i + 1] for i in range (0, len(new_data), 2)}

	params = {'grant_type': 'authorization_code', 'client_id': CLIENT_ID, 'client_secret': CLIENT_SECRET, 'code': data['code'], 'redirect_uri': 'http://127.0.0.1:8080/login'}
	response = requests.post('https://api.intra.42.fr/oauth/token', params=params)
	load = json.loads(response.text)

	response = requests.get('https://api.intra.42.fr/v2/me', headers={'Authorization': f'Bearer {load["access_token"]}'})

	login = json.loads(response.text)['login']
	try:
		query = User.objects.get(username=login)
		return Response(status=status.HTTP_200_OK)
	except:
		data = {}
		data['username'] = login
		data['remote_bool'] = True
		data['remote_token'] = load["access_token"]
		data['password'] = REMOTE_PASSWORD

		serializer = UserSerializer(data=data)
		if (serializer.is_valid()):
			serializer.save()
			return Response({'pk':serializer.data['id']}, status=status.HTTP_201_CREATED, headers={'Access-Control-Allow-Origin':'*'})
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
	if queryset.remote_bool == True:
		return Response({'problem': 'user connected through 42'}, status=status.HTTP_400_BAD_REQUEST)
	if (check_password(data['password'], queryset.password) == True):
		return Response({'pk': queryset.pk}, status=status.HTTP_200_OK, headers={'Access-Control-Allow-Origin':'*'})
	return Response({'problem': 'password'}, status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin':'*'})


@api_view(['GET'])
def UserDetail(request, pk):
	try:
		queryset = User.objects.get(pk=pk)
		serializer = UserSerializer(queryset, context={'request': request}, many=False)
		return Response({'pk': queryset.pk, 'username': queryset.username, 'pfp':serializer.data['pfp'], 'wins': queryset.wins, 'losses': queryset.losses, 'language':queryset.language}, headers={'Access-Control-Allow-Origin':'*'})
	except:
		return Response({'pk':pk}, status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin':'*'})


@api_view(['PATCH', 'POST'])
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
def UserDelete(request, pk):
	try:
		queryset = User.objects.get(pk=pk).delete()
		return Response(status=status.HTTP_200_OK, headers={'Access-Control-Allow-Origin':'*'})
	except:
		return Response(status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin':'*'})


@api_view(['POST'])
def CreateTournament(request, pk):

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


@api_view(['POST'])
def EndGame(request, pk):
	try:
		query = User.objects.get(pk=pk)
	except:
		return Response({'problem': 'user does not exist'}, status=status.HTTP_400_BAD_REQUEST)

	data = (str(request))[(str(request)).index('?') + 1:-2]
	data = data.split("&")
	for i in range (len(data)):
		data[i] = (data[i]).split("=")
	new_data = []
	for lst in data:
		for s in lst:
			new_data.append(s)
	data = {new_data[i]: new_data[i + 1] for i in range (0, len(new_data), 2)}


	data['date'] = str(datetime.now())[:10]
	data['host'] = pk
	data['hostscore'] = int(data['hostscore'])
	data['guestscore'] = int(data['guestscore'])
	if data['guestscore'] > data['hostscore']:
		query.losses = query.losses + 1
		query.elo = query.elo - 20
		query.save()
	elif data['hostscore'] > data['guestscore']:
		query.losses = query.wins + 1
		query.elo = query.elo + 20
		if query.elo > query.best_elo:
			query.best_elo = query.elo
		query.save()
	serializer = GameSerializer(data=data)

	if serializer.is_valid():
		serializer.save()
		return Response(status=status.HTTP_201_CREATED)
	return Response({'problem': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def GameHistory(request, pk):
	try:
		User.objects.get(pk=pk)
	except:
		return Response({'problem': 'user does not exist'}, status=status.HTTP_400_BAD_REQUEST)

	queryset = list(Game.objects.all().filter(host=pk))
	matchList = []
	for g in queryset:
		dico = GameSerializer(g).data
		query = User.objects.get(pk=dico['host'])
		dico['host'] = query.username
		matchList.append(GameSerializer(g).data)

	print(matchList, file=sys.stderr)

	matchList = sorted(matchList, key=lambda x: x['id'], reverse=True)
	return Response({'history': matchList[:5]}, status=status.HTTP_200_OK)


@api_view(['GET'])
def GameFullHistory(request, pk):
	try:
		User.objects.get(pk=pk)
	except:
		return Response({'problem': 'user does not exist'}, status=status.HTTP_400_BAD_REQUEST)

	queryset = list(Game.objects.all().filter(host=pk))
	matchList = []
	for g in queryset:
		dico = GameSerializer(g).data
		query = User.objects.get(pk=dico['host'])
		dico['host'] = query.username
		matchList.append(GameSerializer(g).data)

	matchList = sorted(matchList, key=lambda x: x['pk'], reverse=True)
	return Response({'history': matchList}, status=status.HTTP_200_OK)
