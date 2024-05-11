from django.urls import path
from .views import HomePageView, search_movie_clip

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('search/', search_movie_clip, name='search_movie_clip'),
    # path('search_results/', search_results_view, name='search_results'),  # Add this line
]
