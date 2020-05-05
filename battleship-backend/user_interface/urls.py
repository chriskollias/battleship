from django.urls import path
from .views import *

urlpatterns = [
    path('', main_game_view, name='main-page'),
]