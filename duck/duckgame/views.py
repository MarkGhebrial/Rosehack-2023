from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseForbidden
from duckgame.models import SnakeLeaderboard, ClickerLeaderboard, GalagaLeaderboard
import json

# Create your views here.
def index(request):
    return render(request, "index.html")

def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        redirect(index)
    else:
        pass

def update_leaderboard(request):
    # if not request.user.is_authenticated:
    #     return HttpResponseForbidden('Not authorized')

    # request.user

    return HttpResponse('Testing, testing, 1, 2, 3')

def snake_leaderboard(request):
    # s = SnakeLeaderboard()
    # s.user = 'Mark'
    # s.score = 10
    # s.save()

    out = []
    for score in SnakeLeaderboard.objects.all().values():
        out.append(score)

    return HttpResponse(json.dumps(out))

def clicker_leaderboard(request):
    out = []
    for score in ClickerLeaderboard.objects.all().values():
        out.append(score)

    return HttpResponse(json.dumps(out))

def galaga_leaderboard(request):
    out = []
    for score in GalagaLeaderboard.objects.all().values():
        out.append(score)

    return HttpResponse(json.dumps(out))

def mini(request):
    return render(request, "minigames.html")

def start(request):
    return render(request, "start.html")

def game1(request):
    return render(request, "game1.html")

def game2(request):
    return render(request, "game2.html")

def game3(request):
    return render(request, "game3.html")

def login(request):
    return render(request, "registration/login.html")
