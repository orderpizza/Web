# urls.py
from django.urls import path
from .views import search_movie_clip

urlpatterns = [
    path('search/', search_movie_clip, name='search_movie_clip'),
]
