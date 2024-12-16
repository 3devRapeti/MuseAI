from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
import sys
from .forms import KeywordForm
import pickle
from .models import Users
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

sys.path.append(".")

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

def lyrics(request):
    lyrics = ""

    if request.method == "POST":
        form = KeywordForm(json.loads(request.body))

        # buffer message to show processing
        if not form.is_valid():
            return JsonResponse({"lyrics": "Processing your request. Please wait..."})

        if form.is_valid():
            keyword = form.cleaned_data["Keyword"]
            model = form.cleaned_data["Model"]
            print(keyword)

            return JsonResponse({"lyrics": "Generating lyrics. This may take a few moments..."})
            
            lyrics = generate_lyrics(keyword, model)
            print(lyrics)

            if not lyrics:
                lyrics = (
                    "In a field of dandelions, Underneath the sunny skies, "
                    "Lost in a world of dreams, Where time just passes by. "
                    "Millions of yellow petals, Dancing in the gentle breeze, "
                    "A tranquil sight to behold, A moment of pure peace. "
                    "In this sea of golden beauty, I find myself lost in thought, "
                    "In a field of dandelions, My worries are all but forgot."
                )

            return JsonResponse({"lyrics": lyrics})
        else:
            lyrics = (
                "In a field of dandelions, Underneath the sunny skies, "
                "Lost in a world of dreams, Where time just passes by. "
                "Millions of yellow petals, Dancing in the gentle breeze, "
                "A tranquil sight to behold, A moment of pure peace. "
                "In this sea of golden beauty, I find myself lost in thought, "
                "In a field of dandelions, My worries are all but forgot."
            )
            print(form.errors)
    else:
        form = KeywordForm()

    context = {
        "lyrics": lyrics,
    }
    return render(request, 'lyrics.html', context)

def generate_chords():
    chords = ["C", "G", "Am", "F", "Em", "D", "A", "E"]
    progression = " - ".join(random.sample(chords, 4))
    return f"Chord Progression: {progression}"

def generate_content(request):

    pass

def land(request) :
    if request.method=="POST":
        l=request.POST.get("l")
        id=request.POST.get("id")
        pw=request.POST.get("pass")
        re=request.POST.get("pass2")
        print(re, id, pw)
        if re!="" and re is not None :
            print("signup check")
            re=request.POST.get("pass2")
            if User.objects.filter(username=id).exists():
                print("MATCHED")
                s="An account already exists with this email"
                return render(request,'index.html',{'s':s})
            elif re!=pw:
                print("Unmatched")
                s="Passwords did not match"
                return render(request,'index.html',{'s':s})
            else:
                user=User.objects.create_user(
                    username=id
                )
                user.set_password(pw)
                print(user)
                user.save()
                login(request,user)
                print("logged in")
                return render(request, 'logged_index.html', {'s':"",'user':user,'l':""})
        else:
            if not User.objects.filter(username=id).exists():
                s="Invalid ID"
                return render(request,"index.html",{'s':s})
            user=authenticate(username=id,password=pw)
            if user is None:
                s="Incorrect Password"
                return render(request,"index.html",{'s':s,'l':""})
            else:
                login(request,user)
                print("logged in")
                return render(request, 'logged_index.html',{'s':"",'l':"l"})
    else:
        if request.user.is_authenticated:
            return render(request, 'logged_index.html',{'s':"",'l':""})
        else:
            return render(request, 'index.html',{'s':"",'l':""})

import ast

import boto3

s3 = boto3.resource('s3',
        aws_access_key_id="AKIA2FXAD7FBOXR54K65",
        aws_secret_access_key= "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")

# def read_s3_object(bucket_name, object_key):
#     response = s3.get_object(Bucket=bucket_name, Key=object_key)
#     return response['Body'].read()

# # Example usage:
# bucket_name = 'chordgen'
# object_key = 'chord_predictor_model.pkl'
# data = read_s3_object(bucket_name, object_key)

# print(data)

def chord(request):
    if request.method=='POST':
        model = pickle.loads(s3.Bucket("chordgen").Object("chord_predictor_model.pkl").get()['Body'].read())
        print("1")
        #model = pickle.load(open(s3.get_object('chordgen','chord_predictor_model.pkl'), 'rb'))
        # Load the vectorizer and label encoder
        vectorizer = pickle.load(open(r'C:\Users\tts11\MuseAI\museai\generator\vectorizer.pkl', 'rb'))
        encoder = pickle.load(open(r'C:\Users\tts11\MuseAI\museai\generator\encoder.pkl', 'rb'))
        data=request.POST.get('lyrics')
        X_input = vectorizer.transform([data])
        y_pred = model.predict(X_input)
        predicted_chords = encoder.inverse_transform(y_pred)
        x=predicted_chords.tolist()
        x=ast.literal_eval(x[0])
        print(x)
        x=x[0]
        y=[]
        s=""
        for c in x:
            if c.isupper():
                y.append(s)
                s=c
            else:
                s=s+c
        y.append(s)
        print(y)
        a=y[1]
        b=y[2]
        c=y[3]
        return render(request,'chord.html',{'a':a,'b':b,'c':c})
    else:
        return render(request,'chord.html')

def genre(request):
    if request.method=='POST':
        with open(r'C:\Users/tts11\MuseAI\museai\generator/random_forest_model.pkl', 'rb') as model_file:
            model = pickle.load(model_file)

        with open(r'C:\Users/tts11\MuseAI\museai\generator/tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
            vectorizer = pickle.load(vectorizer_file)

        with open(r'C:\Users/tts11\MuseAI\museai\generator\label_encoder.pkl', 'rb') as le_file:
            label_encoder = pickle.load(le_file)
        lyrics = request.POST.get('lyrics')
        print(lyrics)

        # Transform lyrics using the vectorizer
        lyrics_tfidf = vectorizer.transform([lyrics])

        # Predict the genre using the trained model
        predicted_label = model.predict(lyrics_tfidf)

        # Decode the predicted label to the genre
        predicted_genre = label_encoder.inverse_transform(predicted_label)
        print(predicted_genre[0])
        g = str(predicted_genre[0])
        print(g)
        g="The predicted genre for given lyrics is "+g
        # Return the predicted genre as a JSON response
        # return jsonify({'genre': predicted_genre[0]})
        return render(request,'genre.html',{'genre':g, 'old':lyrics})
    else :
        return render(request,'genre.html',{'genre':"", 'old':""})

def signout(request):
    logout(request)
    return render(request,'index.html',{'s':"",'l':""})