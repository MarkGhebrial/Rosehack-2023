from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseForbidden
from duckgame.models import UserScore
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

def leaderboard_json(request):
    # s = UserScore()
    # s.snakeScore = 99
    # s.save()

    out = []
    for score in UserScore.objects.all().values():
        out.append(score["snakeScore"])        

    return HttpResponse(json.dumps({"snake_scores": out}))

def mini(request):
    return render(request, "minigames.html")

def start(request):
    return render(request, "start.html")
