from django.db import models
import django
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

	REQUIRED_FIELDS = ()
	USERNAME_FIELD = 'username'

	username = models.CharField("username", unique=True, max_length=14, null=True)
	password = models.CharField("password", null=True)
	pfp = models.ImageField("pfp", upload_to='pfp', null=True)
	status = models.IntegerField("status", default=0)
	wins = models.IntegerField("wins", default=0)
	losses = models.IntegerField("losses", default=0)
	elo = models.PositiveIntegerField("elo", default=500)
	best_elo = models.PositiveIntegerField("best_elo", default=500)
	remote_bool = models.BooleanField("remote_bool", default=False)
	remote_token = models.CharField("remote_token", default='')
	is_active = models.BooleanField("is_active", default=True)
	language = models.IntegerField("language", default=0)
	best_rank = models.PositiveIntegerField("best_rank", default=2147483647)
	twoFA = models.BooleanField("twoFA", default=False)
	email = models.EmailField("email", null=True, unique=True)
	key = models.CharField("key", null=True)
	last_game = models.DateTimeField('last_game', null=True)

	def __str__(self):
		return self.username


class Game(models.Model):
	host = models.ForeignKey(User, on_delete=models.CASCADE, related_name="host", null=True)
	guest = models.CharField('guest', max_length=14, null=True)
	hostscore = models.IntegerField('host', default=0)
	guestscore = models.IntegerField('guest', default=0)
	date = models.CharField('date', default='2042-42-42')


class Friend(models.Model):
	player1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="player1", null=True)
	player2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="player2", null=True)
	status = models.IntegerField("status", default=0)


class Tournament(models.Model):
	name = models.CharField('name', null=True)
	description = models.CharField('description', default='')
	capacity = models.IntegerField('capacity', default=16)
	organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="organizer", null=True)
	status = models.IntegerField('status', default=0)


class Contestant(models.Model):
	tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name="tournament", null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user", null=True)
	nickname = models.CharField('nickname', null=True)
	position = models.IntegerField('position', null=True)
	status = models.IntegerField('status', default=1)
	stage = models.IntegerField('stage', default=0)
	score = models.IntegerField('score', default=0)
