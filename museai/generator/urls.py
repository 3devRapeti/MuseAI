from django.urls import path
from .views import generate_content, land, login, signup

urlpatterns = [
    path('', land, name='land'),
    path('login',login, name="login"),
    path('signup', signup, name="signup")
]
