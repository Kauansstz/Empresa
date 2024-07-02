from django.shortcuts import render
from django.core.cache import cache
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
cache.clear()
# Identificar se o usuário existe


def home(request):
    if request.method == "GET":
        return render(request, "pages/home.html")
    else:
        username = request.POST.get("username")
        senha = request.POST.get("password")
        user = authenticate(username=username, password=senha)

        if user:
            login(request, user)
            return render(request, "pages/panel.html")

        else:
            raise Http404("Usuário sem cadastro, favor entrar em contato com a TI")


# Identificar se o usuário existe
# Configuração do Menu
@login_required(login_url="pages/panel.html")
def menu(request):
    return render(request, "pages/panel.html")


@login_required(login_url="pages/performance.html")
def rendimento(request):
    return render(request, "pages/performance.html")


@login_required(login_url="pages/holerite.html")
def holerite(request):
    return render(request, "pages/holerite.html")


# Configuração do Menu


# voltar
def voltar(request):
    request.session.clear()
    return render(request, "index.html")


# voltar
