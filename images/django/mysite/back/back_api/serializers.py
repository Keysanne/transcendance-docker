from rest_framework import serializers
from .models import User, Friend, Tournament, Contestant, Game

class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ('pk',
			'username',
			'password',
			'pfp',
			'status',
			'wins',
			'losses',
			'elo',
			'best_elo',
			'remote_bool',
			'remote_token',
			'is_active',
			'language',
			'best_rank',
			'twoFA',
			'email',
			'key')

	def get_image_url(self, obj):
		request = self.context.get('request')
		photo_url = obj.fingerprint.url
		return request.build_absulute_uri(photo_url)


class GameSerializer(serializers.ModelSerializer):

	class Meta:
		model = Game
		fields = ('pk',
			'host',
			'guest',
			'hostscore',
			'guestscore',
			'date')


class FriendSerializer(serializers.ModelSerializer):

	class Meta:
		model = Friend
		fields = ('pk',
			'player1',
			'player2',
			'status')


class TournamentSerializer(serializers.ModelSerializer):

	class Meta:
		model = Tournament
		fields = ('pk',
			'name',
			'description',
			'capacity',
			'organizer',
			'status')


class ContestantSerializer(serializers.ModelSerializer):

	class Meta:
		model = Contestant
		fields = ('pk',
			'tournament',
			'user',
			'nickname',
			'position',
			'status',
			'status',
			'stage',
			'score')
