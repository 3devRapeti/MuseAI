from django.shortcuts import render
from django.http import HttpResponse
import random
import sys
from .forms import KeywordForm

sys.path.append(".")

from lyrics_generator.generator_gpt2 import generate_lyrics_model

def generate_lyrics(keyWords):
    lyrics = generate_lyrics_model(keyWords)

    return lyrics

def generate_chords():
    chords = ["C", "G", "Am", "F", "Em", "D", "A", "E"]
    progression = " - ".join(random.sample(chords, 4))
    return f"Chord Progression: {progression}"

def generate_content(request):

    lyrics = ""

    if request.method == "POST":

        form = KeywordForm(request.POST)

        if form.is_valid():

            keyword = form.cleaned_data["Keyword"]

            lyrics = generate_lyrics(keyword)
        else:
            print(form.errors)
    else:
        form = KeywordForm()

    chords = generate_chords()

    context = {
        "lyrics": lyrics,
        "chords": chords
    }
    return render(request, 'generate.html', context)

def land(request) :
    return render(request, 'landingpage.html')

def login(request) :
    return render(request,'loginpage.html')

def signup(request) :
    return render(request, 'signuppage.html')

def lyrics(request):
    return render(request,'generate.html')

def chord(request):
    return render(request,'generate.html')

def genre(request):
    return render(request,'generate.html')
