from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Player, Room
from django.template import Context, loader
from .data import Data1, Data2

def post_main(request):
	
	Player.player_number += 1 #플레이 시작하는 화면에서 플레이어를 올립시다 . 일단은 메인에서 확인용으로 
	text = {'num': Player.player_number, 'b': Player.join_number} 
	return render(request, 'game/main.html', text)
#main

def post_explain(request): 
	Player.player_number -= 1
	return render(request, 'game/explain.html')
#game explain

def post_game(request,num):
	
	Player.join_number += 1
	Room.room_number += 1
	if(Player.join_number == 2):
		my_num = Player.player_number
		text = {'a': my_num, 'b': Player.join_number, 'num':Room.room_number}	
	
		return render(request, 'game/game.html', text)
	
	else:
		Player.join_number=1
		my_num = Player.player_number
		text = {'a': my_num, 'b': Player.join_number, 'num':Room.room_number}	
	
		while(Player.join_number ==1):
			pass
		
		return render(request, 'game/game.html', text)
