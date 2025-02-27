from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.shortcuts import redirect,render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from avaliacao_materias.models import Avaliacao
# Create your views here.


def home(request):
    enviado = False
    lista_avaliacoes = Avaliacao.objects.all()

    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET.get('search') #é GET.get() pois é a sintaxe correta para acessar o valor específico que digitamos na search
        lista_avaliacoes = Avaliacao.objects.all().filter(Q(materia__icontains=search_term) | Q(avaliacao__icontains = search_term))
        return render(request,'listar_avaliacoes.html',{'lista_avaliacoes':lista_avaliacoes,'search_term':search_term})


    if request.method == 'POST':
        materia = request.POST.get('materia')
        texto_avaliacao = request.POST.get('avaliacao')
        avaliacao = Avaliacao(materia=materia, avaliacao=texto_avaliacao)
        avaliacao.save()  
        enviado = True
        return redirect('listar_avaliacoes')

    return render(request, 'home.html', {'enviado': enviado, 'lista_avaliacoes': lista_avaliacoes})
    
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

def avaliacoes(request):
    enviado = False
    if request.method == 'POST':
        materia = request.POST.get('materia')
        texto_avaliacao = request.POST.get('avaliacao')
        avaliacao = Avaliacao(materia=materia, avaliacao=texto_avaliacao)
        avaliacao.save()  
        enviado = True
        return redirect('listar_avaliacoes') # esse return é executado quando o método HTTP da requisição é 'POST', ou seja, quando o formulário é submetido. Ele redireciona para a página 'listar_avaliacoes' após o envio do formulário.
    return render(request, 'home.html', {'enviado': enviado}) #Esse return é executado quando o método HTTP da requisição não é 'POST', ou seja, quando a página é acessada normalmente (não por meio de uma submissão de formulário).

def listar_avaliacoes(request):
    lista_avaliacoes = Avaliacao.objects.all()
    return render(request, 'listar_avaliacoes.html',{'lista_avaliacoes':lista_avaliacoes})

def avaliacao(request,id): #para obter a id do objeto. 'pk' = Primary Key
    teste = Avaliacao.objects.get(pk=id)
    print(teste)
    return render(request, 'avaliacao.html',{'teste':teste})