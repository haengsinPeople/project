from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Player
from .profile import Profile, Profile2

def post_main(request): 
	return render(request, 'game/main.html', {})
#main

def post_explain(request): 
	return render(request, 'game/explain.html', {})
#game explain

def post_stay(request):
	Player.player_number += 1
	Player.join_number += 1

	if(Player.join_number == 2):
		text = {'player' : Player.player_number, 'join' :Player.join_number}
		Player.join_number = 0

		return render(request, 'game/game.html', text)
		x
	else:
		text = {'player' : Player.player_number, 'join' :Player.join_number}
	return render(request, 'game/stay.html', text)
		
# stay & give play num
def post_game(request):
    
    return render(request, 'game/game.html', {})


# Create your views here.
