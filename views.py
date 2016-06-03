from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Context, loader
from .models import Player
from .profile import Profile, Profile2

def post_main(request):
	
	Player.player_number += 1
	
	text = {'count' : Player.player_number , 'num' :Player.join_number} 
	return render(request, 'game/main.html', text)

#main

def post_explain(request): 
	return render(request, 'game/explain.html', {})
#game explain

def post_game(request):
	Player.join_number+=1
	waiting = False
	Game_Start = False
	
	
	if(Player.join_number == 2):
		waiting = True
		Game_Start = True
	else:
		waiting = False

	if  waiting == False:
		tpl = loader.get_template('game/stay.html')
		ctx = Context ({ })
	elif waiting == True or Game_Start == True:
		tpl = loader.get_template('game/game.html')
		ctx = Context ({ })
		Player.join_number = 0

	return HttpResponse(tpl.render(ctx))
	
# stay & give play num
def post_stay(request):
    
    return render(request, 'game/game.html', {})


# Create your views here.
