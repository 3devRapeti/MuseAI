from django.shortcuts import render
from django.http import JsonResponse
import random
import sys
import json
from .forms import KeywordForm

sys.path.append(".")

from lyrics_generator.generator_gpt2 import generate_lyrics_model as model_gpt2
from lyrics_generator.generator_OpenAI import generate_lyrics_model as model_openai

def generate_lyrics(keyWords, model):
    lyrics = ""
    if model == "basic":
        lyrics = model_gpt2(keyWords)
    elif model == "premium":
        lyrics = model_openai(keyWords)
    
    return lyrics

def generate_content(request):

    lyrics = ""

    if request.method == "POST":

        form = KeywordForm(json.loads(request.body))
        print(form.is_valid())

        if form.is_valid():

            print(form.cleaned_data)

            keyword = form.cleaned_data["Keyword"]
            print(keyword)
            model = form.cleaned_data["Model"]
            print(model)

            lyrics = generate_lyrics(keyword, model)

            return JsonResponse({"lyrics": lyrics})
        
        else:
            print(form.errors)
    else:
        form = KeywordForm()


    context = {
        "lyrics": lyrics,
    }

    return render(request, 'generate.html', context)
