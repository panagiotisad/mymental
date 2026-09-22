from django import forms
from .models import Rating_data
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# html form for rating data model


class Rating_dataForm(forms.ModelForm):
    class Meta:
        model = Rating_data
        fields = ['mood_rating', 'productivity_rating']
        widgets = {
            'mood_rating': forms.RadioSelect(),
            'productivity_rating': forms.RadioSelect(),
        }

# html form for user registration(User model)


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
