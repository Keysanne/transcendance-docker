from django.db import models
import django

class User(models.Model):
	username = models.CharField("username", unique=True, max_length=14, null=True)
	password = models.CharField("password", null=True)
	pfp = models.ImageField("pfp", upload_to='pfp', null=True)
	status = models.IntegerField("status", default=0)
	wins = models.IntegerField("wins", default=0)
	losses = models.IntegerField("losses", default=0)
	twoFA = models.BooleanField("twoFA", default=False)
	language = models.IntegerField("language", default=1)

class Game(models.Model):
	host = models.ForeignKey(User, on_delete=models.CASCADE, related_name="player1", null=True)
	guest = models.CharField('guest', max_length=14, null=True)
	hostscore = models.IntegerField('host', default=0)
	guestscore = models.IntegerField('guest', default=0)

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
	status = models.IntegerField('status', default=True)
	stage = models.IntegerField('stage', default=0)
	score = models.IntegerField('score', default=0)
