from django.shortcuts import render
from django.http import HttpResponse, Http404
from duckgame.models import SnakeLeaderboard, ClickerLeaderboard, GalagaLeaderboard
import json

def update_leaderboard(request):
    # if not request.user.is_authenticated:
    #     return HttpResponseForbidden('Not authorized')

    # request.user
    return HttpResponse('Testing, testing, 1, 2, 3')

def get_leaderboard(request, game):
    '''Return a JSON list
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

    out = []
    for score in table.objects.all().values():
        out.append(score)

    out = sorted(out, key=lambda d: d["score"], reverse=True)

    return HttpResponse(json.dumps(out))

def serve_file(request, file):
    return render(request, file)
