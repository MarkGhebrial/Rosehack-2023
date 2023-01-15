"""
URL configuration for duck project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from duckgame import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.serve_file, {"file": "index.html"}),
    path('mini', views.serve_file, {"file": "minigames.html"}),
    path('start', views.serve_file, {"file": "start.html"}),
    path('game1', views.serve_file, {"file": "game1.html"}),
    path('game2', views.serve_file, {"file": "game2.html"}),
    path('game3', views.serve_file, {"file": "game3.html"}),

    # API patterns
    path('api/leaderboard/<str:game>', views.leaderboard),
]
