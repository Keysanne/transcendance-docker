from rest_framework import serializers
from .models import User, Friend, Tournament, Contestant

class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = '__all__'

	def get_image_url(self, obj):
		request = self.context.get('request')
		photo_url = obj.fingerprint.url
		return request.build_absulute_uri(photo_url)


class FriendSerializer(serializers.ModelSerializer):

	class Meta:
		model = Friend
		fields = '__all__'


class TournamentSerializer(serializers.ModelSerializer):

	class Meta:
		model = Tournament
		fields = '__all__'


class ContestantSerializer(serializers.ModelSerializer):

	class Meta:
		model = Contestant
		fields = '__all__'
