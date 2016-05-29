from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world")

def post_main(request):
    return render(request, 'game/main.html', {})
def post_explain(request):
    return render(request, 'game/explain.html', {})
def post_game(request):
    return render(request, 'game/game.html', {})
def post_stay(request):
    return render(request, 'game/stay.html', {})
def post_login(request):
    return render(request, 'game/login.html', {})
# Create your views here.
