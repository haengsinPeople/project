from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Player, Room
from django.views.decorators.csrf import csrf_exempt
from django.template import Context, loader
from .Davinci import *
@csrf_exempt
def post_main(request):
	
	if request.session.get('nickname',) != None:
		return redirect('/game')

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
			return HttpResponse("<script>alert('닉네임을 입력하지 않았습니다. 다시 입력해주세요.'); history.go(-1);</script>");
		except:
			return HttpResponse("<script>alert('이미 존재하는 닉네임입니다. 다른 닉네임을 입력해주세요.'); history.go(-1);</script>");
	        
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
				return HttpResponse("<script>alert('이미 다른 방에 참여하고 있습니다.'); history.go(-1);</script>");
			else:#다른 방에 조인하지 않았다면,
				player.is_joined = True
			if room.current_player_number == 2:
				match_player.save()
				room.is_playing = True
			elif is_entered == False:
				player.is_joined = True
				room.join_players.add(player)
				room.player_number += 1
		elif is_enter == False:
			return HttpResponse("<script>alert('이미 시작된 방입니다. 다른 방을 이용해주세요.'); history.go(-1);</script>");
	except:
		return HttpResponse("오류발생")

	if room.is_playing == True:
		#게임 시작
		wait = False
	else:
		wait = True

	ctx = Context({'player' : player, 'match_player' : match_player, 'room' : room,})

	if wait == False:
		#게임 종료, 게임 중 
		tpl = loader.get_template('game/game.html')

	elif wait == True:
		tpl = loader.get_template('game/wait.html')
		ctx = Context({})

	player.save()
	room.save()
	
		
	return HttpResponse(tpl.render(ctx))

