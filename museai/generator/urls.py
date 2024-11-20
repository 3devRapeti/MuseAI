from django.urls import path
from .views import generate_content, land, login, signup, lyrics, chord, genre

urlpatterns = [
    path('', land, name='land'),
    path('login',login, name="login"),
    path('signup', signup, name="signup"),
    path('generate', generate_content, name='generate'),
    path('lyrics', lyrics, name="lyrics"),
    path('chord',chord,name="chord"),
    path('genre',genre,name="genre"),
]
