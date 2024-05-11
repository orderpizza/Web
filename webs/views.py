# views.py
from django.shortcuts import render
from .forms import KoreanSentenceForm
from .models import MovieClip
from django.views.generic import TemplateView
import os

def search_movie_clip(request):
    if request.method == 'POST':
        form = KoreanSentenceForm(request.POST)
        if form.is_valid():
            korean_sentence = form.cleaned_data['korean_sentence']
            # Query the database
            movie_clips = MovieClip.objects.filter(korean_sentence__icontains=korean_sentence)
            urls = [os.path.join('C:\\Users\\lseun\\Desktop\\Web\\split_clips', clip.filename) for clip in movie_clips]
            return render(request, 'search_results.html', {'urls': urls})
    else:
        form = KoreanSentenceForm()
    return render(request, 'search_form.html', {'form': form})


class HomePageView(TemplateView):
    template_name = 'home.html'