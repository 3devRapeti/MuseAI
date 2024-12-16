from django.urls import path
from .views import generate_content, land, lyrics, chord, genre, signout

urlpatterns = [
    path('', land, name='land'),
    path('generate', generate_content, name='generate'),
    path('lyrics', lyrics, name="lyrics"),
    path('chord',chord,name="chord"),
    path('genre',genre,name="genre"),
    path('signout',signout,name="signout"),
]
