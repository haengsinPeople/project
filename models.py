
from django.db import models
#charfield() char
#integerfield() number
#

class Card(models.Model):
	Index = models.IntegerField(default = 0, null = False)
	Number = models.CharField(max_length = 10, null = False)
	Color = models.CharField(max_length = 10, null = False)
	Is_finded = models.IntegerField(default = 0, null =False)

class Player(models.Model):
    nickname = models.CharField(max_length = 20, null = True, unique = True)
    is_joined = models.BooleanField(default = False, null = False)
    Turn = models.BooleanField(default = False, null = False)
    Finded = models.IntegerField(default = 0, null = False)
    Num_of_joker = models.IntegerField(default = 0, null = False)
    Last_card = models.IntegerField(default = 0, null = False)
    Get_pos = models.IntegerField(default = 0, null = False)
    Hand = models.ManyToManyField(Card)
    Hand_cnt = models.IntegerField(default = 0, null = False)
    def __str__(self):
                return self.nickname
                
class Room(models.Model):
	name = models.CharField(max_length = 40, null = True, unique = True)
	join_players = models.ManyToManyField(Player)
	is_playing = models.BooleanField(default = False, null = False)
	player_number = models.IntegerField(default = 0, null = False)
	Deck = models.ManyToManyField(Card)
	Deck_cnt = models.IntegerField(default = 0, null = False)
	def __str__(self):
                return self.name


