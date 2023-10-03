from django.shortcuts import render
from . models import*
# Create your views here.

def continente(request):
    consulta = {
        'consultas': Continente.objects.all()
    }
    return render(request, 'consulta/continente.html', consulta)

def nacionalidade(request):
    consulta = {
        'consultas': Nacionalidade.objects.all()
    }
    return render(request, 'consulta/nacionalidade.html', consulta)

def pais(request):
    consulta = {
        'consultas': Pais.objects.all()
    }
    return render(request, 'consulta/pais.html', consulta)

def episodio(request):
    consulta = {
        'consultas': Episodio.objects.all()
    }
    return render(request, 'consulta/episodio.html', consulta)

def temporada(request):
    consulta = {
        'consultas': Temporada.objects.all()
    }
    return render(request, 'consulta/temporada.html', consulta)

def genero(request):
    consulta = {
        'consultas': Genero.objects.all()
    }
    return render(request, 'consulta/genero.html', consulta)

def ator(request):
    consulta = {
        'consultas': Ator.objects.all()
    }
    return render(request, 'consulta/ator.html', consulta)

def diretor(request):
    consulta = {
        'consultas': Diretor.objects.all()
    }
    return render(request, 'consulta/diretor.html', consulta)

def serie(request):
    consulta = {
        'consultas': Serie.objects.all()
    }
    return render(request, 'consulta/serie.html', consulta)

def serieepisodio(request):
    consulta = {
        'consultas': SerieEpisodio.objects.all()
    }
    return render(request, 'consulta/serieepisodio.html', consulta)

def filme(request):
    consulta = {
        'consultas': Filme.objects.all()
    }
    return render(request, 'consulta/filme.html', consulta)

def filmeator(request):
    consulta = {
        'consultas': FilmeAtor.objects.all()
    }
    return render(request, 'consulta/filmeator.html', consulta)

def reserva(request):
    reserva = {
        'consultas': Filme.objects.all()
    }
    return render(request, 'reserva/reserva.html', reserva)