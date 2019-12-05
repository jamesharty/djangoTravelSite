from django.contrib.auth import login, authenticate
from django.contrib import  auth
from django.shortcuts import render, redirect
from packages.views import featurePackages
from accounts.forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.firstName = form.cleaned_data.get('firstName')
            user.profile.lastName = form.cleaned_data.get('lastName')
            user.profile.cardNumber = form.cleaned_data.get('cardNumber')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect(featurePackages)
    else:
        form = SignUpForm()
    return render(request, 'pages/signup.html', {'form': form})




