from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from User.models import Profile, Record

# Create your views here.

def access(request):
  user = authenticate(request, username=request.POST['username'], password=request.POST['pass'])
  if user is not None:
    login(request, user)
    return redirect('dashboard:home')
  else:
    messages.error(request, 'Senha ou Usuário incorreto')
    return redirect('/login')

@login_required(login_url='/login')
def home(request):
  # try:
    profile = Profile.objects.get(user=request.user)
    friends = Profile.objects.filter(user=request.user)
    records = Record.objects.filter(user=profile)
    return render(request, 'user/index.html', {
      'profile': profile, 
      'friends': friends, 
      'recore': records
      })
  # except:
  #   messages.error(request, 'Página somente acessível para membros!')
  #   return redirect('/login')
  
def users(request):
  users = User.objects.filter(is_staff=False).exclude(id = user.id)
  return render(request, 'user/users.html', {'users': users, 'user': user})

def registers_index(request):
  user = get_object_or_404(User, id=request.session['user.id'])
  return render(request, 'user/record.html', {'user': user})

def registers(request):
  user = get_object_or_404(User, id=request.session['user.id'])
  return render(request, 'user/list/record.html', {'user': user})

def registers_public(request):
  user = get_object_or_404(User, id=request.session['user.id'])
  return render(request, 'user/records.html', {'user': user})

def register_create(request):
  user = get_object_or_404(User, id=request.session['user.id'])
  return render(request, 'user/create_record.html', {'user': user})

def account(request):
  user = get_object_or_404(User, id=request.session['user.id'])
  return render(request, 'user/account.html', {'user': user})