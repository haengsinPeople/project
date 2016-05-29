from django.db import models
from django.utils import timezone

class Card(models.Model):
    Color = models.CharField(max_length = 2, null = False)
    Number = models.CharField(max_length = 5, null = False)
    Is_match = models.BooleanField(default = False, null = False)

class Player(models.Model):
    Name = models.CharField(max_length = 20, null = False, unique = True)
    Hand = models.ManyToManyField(Card)
    Location = models.PositiveIntegerField()
    Number = models.PositiveIntegerField()
    Turn = models.BooleanField(default = False, null = False)
	
class Room(models.Model):
    RoomName = models.CharField(max_length = 20, null = False, unique = True)
    Num_of_player = models.PositiveIntegerField()
    Is_start = models.BooleanField(default = False, null = False)
    Deck = models.ForeignKey(Card)
