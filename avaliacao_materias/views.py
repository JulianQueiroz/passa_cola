from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect,render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request,'home.html')

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'registration/cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponse('Já existe um usuário com esse username')

        user = User.objects.create_user(username=username,email=email,password=senha)
        user.save()
        return HttpResponse('Cadastrado com sucesso')
