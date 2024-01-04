from rest_framework import serializers
from .models import User, Friend, Tournament, Contestant

class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ['pk', 'username', 'password', 'pfp', 'status', 'wins', 'losses', 'twoFA', 'language', 'elo', 'best_elo', 'best_rank']

	def get_image_url(self, obj):
		request = self.context.get('request')
		photo_url = obj.fingerprint.url
		return request.build_absulute_uri(photo_url)


class FriendSerializer(serializers.ModelSerializer):

	class Meta:
		model = Friend
		fields = ['pk', 'player1', 'player2', 'status']


class TournamentSerializer(serializers.ModelSerializer):

	class Meta:
		model = Tournament
		fields = ['pk', 'name', 'description', 'capacity', 'organizer', 'status']


class ContestantSerializer(serializers.ModelSerializer):

	class Meta:
		model = Contestant
		fields = ['pk', 'tournament', 'user', 'nickname', 'position', 'status', 'stage', 'score']
