from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    firstName = forms.CharField(max_length=30, required=True)
    lastName = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    cardNumber = forms.CharField(max_length=254, help_text='Required. Enter Card Number')

    class Meta:
        model = User
        fields = ('username', 'firstName', 'lastName', 'email', 'cardNumber', 'password1', 'password2', )