from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Player, Room, Card
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
	Num.number += 1
	session_nickname = request.session.get('nickname',)
	if session_nickname == None:
		return redirect('/')
    
	rooms = Room.objects.all()
	tpl = loader.get_template('game/stay.html')
	ctx = Context({'rooms' : rooms, 'nickname' : session_nickname, 'number':Num.number})
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
		i = 0
		while i < 24:##덱 초기화
			new_card = Card.objects.get(Index = i)
			room.Deck.add(new_card)
			room.Deck_cnt += 1
			room.save()
			i += 1

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
			else:
				player.is_joined = True
			if room.player_number == 2:
				player.Hand_cnt = 0
				match_player.Hand_cnt = 0
				## player
				i = 0
				while i < 4:
					player_card_index = draw(room.Deck_cnt)
					player_new_card = room.Deck.order_by('Index')[player_card_index]
					player.Hand.add(player_new_card)
					player.Hand_cnt += 1
					room.Deck_cnt -= 1
					room.Deck.remove(player_new_card)
					i += 1

				##match_player
				i = 0
				while i < 4:
					player_card_index = draw(room.Deck_cnt)
					player_new_card = room.Deck.order_by('Index')[player_card_index]
					match_player.Hand.add(player_new_card)
					match_player.Hand_cnt += 1
					room.Deck_cnt -= 1
					room.Deck.remove(player_new_card)
					i += 1
				SetTurn(player,match_player)
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
		if player.Turn == 1:
			player_card_index = draw(room.Deck_cnt)
			player_new_card = room.Deck.order_by('Index')[player_card_index]
			player.Hand.add(player_new_card)
			Draw_Num = player_new_card.Number
			player.Hand_cnt += 1
			room.Deck_cnt -= 1
			room.Deck.remove(player_new_card)
			player.Turn += 1
		elif player.Turn > 1:

				if match_player.Hand.order_by('Index')[int(request.GET.get('select'))-1].Number == request.GET.get('num'):
					match_player.save()
					player.Turn += 1
				else:
					room.player[0][1] = 1
					if player.Turn == 0:
						match_player.Turn = 1
						plyer.Turn = 0
					else:
						player.Turn = 0
						match_player.Turn = 1
					match_player.save()

				if request.GET.get('num') == '12':
					if player.Turn == 0:
						match_player.Turn = 1
						plyer.Turn = 0
					else:
						player.Turn = 0
						match_player.Turn = 1
					match_player.save()


		wait = False
	else:
		wait = True

	ctx = Context({'player' : player, 'match_player' : match_player, 'room' : room, 'num' : request.GET.get('num'), 'select' : request.POST.get('select'), })

	if wait == False:
		#게임 종료, 게임 중 
		tpl = loader.get_template('game/game.html')

	elif wait == True:
		tpl = loader.get_template('game/wait.html')
		ctx = Context({})

	player.save()
	room.save()
	
		
	return HttpResponse(tpl.render(ctx))

