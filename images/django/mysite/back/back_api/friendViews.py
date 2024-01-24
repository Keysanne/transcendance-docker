from django.shortcuts import render
from .models import User, Friend
from rest_framework import generics
from .serializers import UserSerializer, FriendSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def createRequest(request, pk, username):
	try:
		player1 = User.objects.get(pk=pk)
		player2 = User.objects.get(username=username)
		if (player1 == player2):
			return Response({'problem':'same person'}, status=status.HTTP_409_CONFLICT, headers={'Access-Control-Allow-Origin':'*'})
	except:
		return Response({'problem':'does not exist'},status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin':'*'})
	try:
		queryset = Friend.objects.get(player1=player1, player2=player2)
		return Response(status=status.HTTP_409_CONFLICT, headers={'Access-Control-Allow-Origin':'*'})
	except:
		pass
	try:
		queryset = Friend.objects.get(player1=player2, player2=player2)
		return Response(status=status.HTTP_409_CONFLICT, headers={'Access-Control-Allow-Origin':'*'})
	except:
		serializer = FriendSerializer(data={'player1':player1.pk, 'player2':player2.pk})
		if serializer.is_valid():
			serializer.save()
			return Response(status=status.HTTP_201_CREATED, headers={'Access-Control-Allow-Origin':'*'})
		return Response({'problem':serializer.errors}, status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin':'*'})


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def acceptRequest(request, pk, username):
	try:
		player1 = User.objects.get(pk=pk)
		player2 = User.objects.get(username=username)
		if (player1 == player2):
			return Response({'problem':'same person'}, status=status.HTTP_409_CONFLICT, headers={'Access-Control-Allow-Origin':'*'})
	except:
		return Response({'problem':'player does not exist'},status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin':'*'})
	try:
		queryset = Friend.objects.get(player1=player2, player2=player1)
		queryset.status = 1
		queryset.save()
		return Response(status=status.HTTP_200_OK, headers={'Access-Control-Allow-Origin':'*'})
	except:
		return Response({'problem':'request does not exist'},status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin':'*'})


@api_view(['DELETE'])
@permission_classes((IsAuthenticated, ))
def denyRequest(request, pk, username):
	try:
		player1 = User.objects.get(pk=pk)
		player2 = User.objects.get(username=username)
		if (player1 == player2):
			return Response({'problem':'same person'}, status=status.HTTP_409_CONFLICT, headers={'Access-Control-Allow-Origin':'*'})
	except:
		return Response({'problem':'player does not exist'},status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin':'*'})
	try:
		queryset = Friend.objects.get(player1=player2, player2=player1).delete()
		return Response(status=status.HTTP_200_OK, headers={'Access-Control-Allow-Origin':'*'})
	except:
		return Response({'problem':'request does not exist'},status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin':'*'})


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def blockRequest(request, pk, username):
	try:
		player1 = User.objects.get(pk=pk)
		player2 = User.objects.get(username=username)
		if (player1 == player2):
			return Response({'problem':'same person'}, status=status.HTTP_409_CONFLICT, headers={'Access-Control-Allow-Origin':'*'})
	except:
		return Response({'problem':'player does not exist'},status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin':'*'})
	try:
		queryset = Friend.objects.get(player1=player2, player2=player1)
		queryset.status = 2
		queryset.save()
		return Response(status=status.HTTP_200_OK, headers={'Access-Control-Allow-Origin':'*'})
	except:
		return Response({'problem':'request does not exist'},status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin':'*'})


@api_view(['DELETE'])
@permission_classes((IsAuthenticated, ))
def unfriend(request, pk, username):
	try:
		player1 = User.objects.get(pk=pk)
		player2 = User.objects.get(username=username)
		if (player1 == player2):
			return Response({'problem':'same person'}, status=status.HTTP_409_CONFLICT, headers={'Access-Control-Allow-Origin':'*'})
	except:
		return Response({'problem':'player does not exist'},status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin':'*'})
	try:
		queryset = Friend.objects.get(player1=player1, player2=player2, status=1).delete()
		return Response(status=status.HTTP_200_OK, headers={'Access-Control-Allow-Origin':'*'})
	except:
		pass
	try:
		queryset = Friend.objects.get(player1=player2, player2=player1, status=1).delete()
		return Response(status=status.HTTP_200_OK, headers={'Access-Control-Allow-Origin':'*'})
	except:
		return Response({'problem':'request does not exist'},status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin':'*'})


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def viewRequest(request, pk):
	listofpending = []

	try:
		queryset = User.objects.get(pk=pk)
	except:
		return Response(status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin':'*'})

	try:
		queryset = Friend.objects.all().filter(player2=pk, status=0)

		for user in list(queryset):
			friend = FriendSerializer(user, many=False)
			req = User.objects.get(pk=friend.data["player1"])
			serial = UserSerializer(req, context={'request': request}, many=False)
			listofpending.append({'username':serial.data["username"], 'pfp':serial.data["pfp"], 'elo':serial.data["elo"]})
	except:
		pass

	return Response({'pending':listofpending}, status=status.HTTP_200_OK, headers={'Access-Control-Allow-Origin':'*'})


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def listRequest(request, pk):
	listoffriends = []

	try:
		queryset = User.objects.get(pk=pk)
	except:
		return Response(status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin':'*'})

	try:
		queryset = Friend.objects.all().filter(player2=pk, status=1)

		for user in list(queryset):
			friend = FriendSerializer(user, many=False)
			req = User.objects.get(pk=friend.data["player1"])
			serial = UserSerializer(req, context={'request': request}, many=False)
			listoffriends.append({'username':serial.data["username"], 'pfp':serial.data["pfp"], 'elo':serial.data["elo"], 'status': serial.data["status"]})
	except:
		pass

	try:
		queryset = Friend.objects.all().filter(player1=pk, status=1)

		for user in list(queryset):
			friend = FriendSerializer(user, many=False)
			req = User.objects.get(pk=friend.data["player2"])
			serial = UserSerializer(req, context={'request': request}, many=False)
			listoffriends.append({'username':serial.data["username"], 'pfp':serial.data["pfp"], 'elo':serial.data["elo"], 'status': serial.data["status"]})
	except:
		pass

	return Response({'friends':listoffriends}, status=status.HTTP_200_OK, headers={'Access-Control-Allow-Origin':'*'})
