from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def mini(request):
    return render(request, "minigames.html")

def start(request):
    return render(request, "start.html")
