from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Player, Room
from django.views.decorators.csrf import csrf_exempt
from django.template import Context, loader
from .Davinci import *
from django.utils import timezone

@csrf_exempt
def post_main(request):
	
	if request.session.get('nickname',) != None:
		return redirect('/')

	tpl = loader.get_template('game/main.html')
	ctx = Context({})

	return HttpResponse(tpl.render(ctx))
#main

@csrf_exempt
def post_explain(request): 
	if request.session.get('nickname',) == None:
		try:
			nickname = False
			nickname = request.POST['nickname']
			nickname = nickname.strip()
			if nickname == '':
				raise NameError
			new_player = Player(nickname = nickname)
			new_player.save()
			request.session['nickname'] = nickname

		except NameError:
			return HttpResponse("<script>alert('nonickname'); history.go(-1);</script>");
		except:
			return HttpResponse("<script>alert('already nickname,,other nickname'); history.go(-1);</script>");
	        
	tpl = loader.get_template('game/explain.html')
	ctx = Context({})

	return HttpResponse(tpl.render(ctx))
#game explain

@csrf_exempt
def post_stay(request):
	session_nickname = request.session.get('nickname',)

	if session_nickname == None:
		return redirect('/')
    
	rooms = Room.objects.all()
	tpl = loader.get_template('game/stay.html')
	ctx = Context({
	'rooms' : rooms
	})
		
	return HttpResponse(tpl.render(ctx))

@csrf_exempt
def room_list(request):

    session_nickname = request.session.get('nickname',)

    if session_nickname == None:
        return redirect('/index')
    
    rooms = Room.objects.all()
    tpl = loader.get_template('game/room_list.html')
    ctx = Context({
    'rooms' : rooms
    })
		
    return HttpResponse(tpl.render(ctx))


@csrf_exempt
def post_game(request, name):
	session_nickname = request.session.get('nickname', )
	match_player = False
	wait = False

	if session_nickname == None:
		return redirect('/game')

	try:
		room = Room.objects.get(name = name)

	except:
		new_room = Room(name = name)
		new_room.save()
		room = Room.objects.get(name = name)

	try:
		player = Player.objects.get(nickname = session_nickname)
		is_enter = False

		for room_player in room.join_players.all():
            
			if room_player.nickname == session_nickname:
				is_enter = True
			else:
				match_player = room_player


		if room.is_playing == False:
			if player.is_joined and is_entered == False:
				return HttpResponse("<script>alert('already room'); history.go(-1);</script>");
			else:
				player.is_joined = True
			if room.current_player_number == 2:
				match_player.save()
				room.is_playing = True
			elif is_entered == False:
				player.is_joined = True
				room.join_players.add(player)
				room.player_number += 1
		elif is_enter == False:
			return HttpResponse("<script>alert('already start room'); history.go(-1);</script>");
	except:
		return HttpResponse("error")

	if room.is_playing == True:
		
		wait = False
	else:
		wait = True

	ctx = Context({'player' : player, 'match_player' : match_player, 'room' : room,})

	if wait == False:
		
		tpl = loader.get_template('game/game.html')

	elif wait == True:
		tpl = loader.get_template('game/wait.html')
		ctx = Context({})

	player.save()
	room.save()
	
		
	return HttpResponse(tpl.render(ctx))


@csrf_exempt
def room(request):
	if request.session.get('name',) == None:
		try:
			name = False
			name = request.POST['name']
			name = name.strip()
			if name == '':
				raise NameError
			new_Room = Room(name = name)
			new_Room.save()
			request.session['name'] = name

		except NameError:
			return HttpResponse("<script>alert('nonickname'); history.go(-1);</script>");
		except:
			return HttpResponse("<script>alert('already nickname,,other nickname'); history.go(-1);</script>");
	        
	tpl = loader.get_template('game/room.html')
	ctx = Context({})

	return HttpResponse(tpl.render(ctx))