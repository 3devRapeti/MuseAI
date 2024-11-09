from django.shortcuts import render
from django.http import HttpResponse
import random
import sys

sys.path.append(".")

from generator_call_OpenAI.generator import generate_lyrics_model

def generate_lyrics(keyWords):

    lyrics = generate_lyrics_model(keyWords)

    return lyrics

def generate_chords():
    chords = ["C", "G", "Am", "F", "Em", "D", "A", "E"]
    progression = " - ".join(random.sample(chords, 4))
    return f"Chord Progression: {progression}"

def generate_content(request):

    keyWords = ["rain", "love"]

    lyrics = generate_lyrics(keyWords)

    chords = generate_chords()

    context = {
        "lyrics": lyrics,
        "chords": chords
    }

    return render(request, 'generate.html', context)
