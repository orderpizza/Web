from django.db import models

class MovieClip(models.Model):
    filename = models.CharField(max_length=100)
    start_time = models.CharField(max_length=20)
    end_time = models.CharField(max_length=20)
    korean_sentence = models.TextField()
