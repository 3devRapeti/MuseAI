from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

# AI functions for generating lyrics and chords
def generate_lyrics():
    return "These are some generated lyrics."

def generate_chords():
    return "C G Am F"

def home(request):
    return HttpResponse("Welcome to the MuseAI Project!")

def generate_content(request):
    lyrics = generate_lyrics()
    chords = generate_chords()
    return JsonResponse({'lyrics': lyrics, 'chords': chords})
