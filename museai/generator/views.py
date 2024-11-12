from django.shortcuts import render
from django.http import HttpResponse
import random

def generate_lyrics():
    lines = [
        "चाँदनी रात में, तेरे ख्वाबों में खोया",
        "तेरे बिना अधूरा, मेरा हर सपना",
        "तू है तो सब कुछ है, तू नहीं तो कुछ नहीं",
        "तेरी यादों में बसा, मेरा हर मौसम",
        "पलकों पर रखा मैंने तेरा नाम",
        "दिल की धड़कन में बसी है ये ख़ामोशी",
        "तेरे संग जिया मेरा, हर पल जैसे एक ख़्वाब",
        "तेरा साथ मिले तो, हर मुश्किल है आसान"
    ]
    return "\n".join(random.sample(lines, 3))

def generate_chords():
    chords = ["C", "G", "Am", "F", "Em", "D", "A", "E"]
    progression = " - ".join(random.sample(chords, 4))
    return f"Chord Progression: {progression}"

def generate_content(request):
    lyrics = generate_lyrics()
    chords = generate_chords()

    context = {
        "lyrics": lyrics,
        "chords": chords
    }
    return render(request, 'generate.html', context)
