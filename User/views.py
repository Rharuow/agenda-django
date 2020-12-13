from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, logout as django_logout, login as login_auth
from .models import Profile
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.

def login(request):
  return render(request, 'session/login.html')

def logout(request):
  django_logout(request)
  return redirect('/')

def signup(request):
  return render(request, 'session/signup.html')

def new(request):
  if(request.POST['pass'] == request.POST['pass_confirm']):
    user = User.objects.create(
      username = request.POST['username'],
      email = request.POST['email']
    )

    user.set_password(request.POST['pass'])

    user.save()

    profile = Profile.objects.create(user=user)
    
    messages.success(request, 'Usuário cadastrado com sucesso')
    return redirect('/')
  messages.error(request, 'Senhas não conferem!')
  return redirect('signup')