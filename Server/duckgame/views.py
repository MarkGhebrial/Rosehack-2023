from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseBadRequest, HttpResponseForbidden
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from duckgame.models import SnakeLeaderboard, ClickerLeaderboard, GalagaLeaderboard
import json

def serve_file(request, file):
    return render(request, file)

def auth(request):
    if request.method == "POST":
        data = request.POST
        user = authenticate(request, username=data["name"], password=data["password"])
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return HttpResponse("Invalid login. Are the username and password correct?")
    else:
        return HttpResponseBadRequest()

def new_user(request):
    if request.method == "POST":
        data = request.POST
        user = User.objects.create_user(username=data["name"], password=data['password'])
        user.save()

        return auth(request)
    else:
        return HttpResponseBadRequest()

def logout_view(request):
    logout(request)
    return redirect("/")

def leaderboard(request, game):
    '''
    If a GET request: Return a JSON list of leaderboard entries for the specified game,
    sorted from highest to lowest score.

    If a POST request: Add the supplied leaderboard entry to the leaderboard.
    '''

    table = None
    if game == 'snake':
        table = SnakeLeaderboard
    elif game == 'clicker':
        table = ClickerLeaderboard
    elif game == 'galaga':
        table = GalagaLeaderboard
    else:
        raise Http404()

    # Get the leaderboard data
    if request.method == "GET":
        out = []
        for score in table.objects.all().values():
            out.append(score)

        out = sorted(out, key=lambda d: d["score"], reverse=True)

        return HttpResponse(json.dumps(out))

    # Upload data to the leaderboard, an example request looks like the following:
    # requests.post("http://localhost:8000/api/leaderboard/galaga", data={'user':'Mark','score':10})
    elif request.method == "POST":
        data = request.POST

        if not request.user.is_authenticated:
            return HttpResponseForbidden()

        if not 'score' in data.keys():
            return HttpResponseBadRequest("Provide a score field")

        # Make sure the score field is an integer
        try:
            int(data['score'])
        except:
            return HttpResponseBadRequest("Score must be an integer")

        for entry in table.objects.all():
            if entry.user == request.user.username: # Find the user's leaderboard entry
                if int(data['score']) <= entry.score:
                    return HttpResponse("No personal best")

        # Write to the database
        d = table()
        d.user = request.user.username
        d.score = data['score']
        d.save()

        return HttpResponse("New personal best!")

    else:
        raise HttpResponseBadRequest()
