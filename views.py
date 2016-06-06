from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Player, Room
from django.views.decorators.csrf import csrf_exempt
from django.template import Context, loader
@csrf_exempt
def post_main(request): 
	
	if request.session.get('nickname',) != None: #닉네임이 없을 경우
		return redirect('/game')  #game으로 돌려보냄

	tpl = loader.get_template('game/main.html') #불러온다 
	ctx = Context({}) #context파일

	return HttpResponse(tpl.render(ctx))
#main

@csrf_exempt
def post_explain(request): 
	if request.session.get('nickname',) == None:
		try:
			nickname = False
			nickname = request.POST['nickname']
			if nickname == '': #닉네임을 입력하지 않은 경우
				raise NameError 
			new_player = Player(nickname = nickname) 
			new_player.save()
			request.session['nickname'] = nickname

		except NameError: #닉네임 입력 X
			return HttpResponse("<script>alert('닉네임을 입력하지 않았습니다. 다시 입력해주세요.'); history.go(-1);</script>");
		except: #닉네임이 존재할 경우
			return HttpResponse("<script>alert('이미 존재하는 닉네임입니다. 다른 닉네임을 입력해주세요.'); history.go(-1);</script>");
	        
	tpl = loader.get_template('game/explain.html') #넘어감
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
	ctx = Context({'rooms' : rooms, 'nickname' : session_nickname })
		
	return HttpResponse(tpl.render(ctx))


@csrf_exempt
def post_game(request, name):
	session_nickname = request.session.get('nickname', )
	match_player = False
	wait = False
	Room.number += 1
	number = Room.number

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
			if player.is_joined and is_enter == False:
				return HttpResponse("<script>alert('이미 다른 방에 참여하고 있습니다.'); history.go(-1);</script>");
			else:#다른 방에 조인하지 않았다면,
				player.is_joined = True
			if room.player_number == 2:
				match_player.save()
				room.is_playing = True
			elif is_enter == False:
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

	ctx = Context({'player' : player, 'match_player' : match_player, 'room' : room, 'number' : number})

	if wait == False:
		#게임 종료, 게임 중 
		tpl = loader.get_template('game/game.html')

	elif wait == True:
		tpl = loader.get_template('game/wait.html')
		ctx = Context({})

	player.save()
	room.save()
	
		
	return HttpResponse(tpl.render(ctx))