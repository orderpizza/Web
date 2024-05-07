# forms.py
from django import forms

class KoreanSentenceForm(forms.Form):
    korean_sentence = forms.CharField(label='Enter a Korean sentence', max_length=200)
