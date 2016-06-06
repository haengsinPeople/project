from django.db import models
#charfield() char
#integerfield() number
#
class Player(models.Model):
    nickname = models.CharField(max_length = 20, null = True, unique = True)
    is_joined = models.BooleanField(default = False, null = False)
    def __str__(self):
                return self.nickname

class Room(models.Model):
	name = models.CharField(max_length = 40, null = True, unique = True)
	join_players = models.ManyToManyField(Player)
	number = 0
	is_playing = models.BooleanField(default = False, null = False)
	player_number = models.IntegerField(default = 0, null = False)
	def __str__(self):
                return self.name