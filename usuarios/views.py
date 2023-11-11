from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required

def cadastro(request):
    if request.method == "GET" :
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('usernamelogin')
        email = request.POST.get('emaillogin')
        senha = request.POST.get('senhalogin')
        
        user = User.objects.filter(username=username).first()
        
        if user:
            return HttpResponse('Já existe um usuário com esse nome')
        else:
            user = User.objects.create_user(username=username, email=email, password=senha)
            user.save()
        
        return HttpResponse('Usuário cadastrado com sucesso')
    
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('usernamelogin')
        senha = request.POST.get('senhalogin')
        
    user = authenticate(username=username, password=senha)
    
    if user:
        login_django(request, user)
        return HttpResponse('Autenticado')
    else:
        return HttpResponse('User ou senha invalídos')
    
@login_required(login_url="/auth/login/")      
def plataforma(request):
    return HttpResponse('Logado na Plataforma')
