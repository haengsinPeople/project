from django.db import models
#charfield() char
#integerfield() number
#

class Player(models.Model):
    player_number = 0
    join_number = 0
    player_data = 0

class Room(models.Model):
	room_number = 0