from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return render(request,'accueil.html')

def download_resume(request):
    return render(request,'accueil.html',{
    'cv_file' : 'resume.pdf'
    })

def parcours_scolaire(request):
    return render(request, 'parcours_scolaire.html')

def projets(request):
    return render(request, 'projets.html')

def devine_nombre(request):
    return render(request, 'projet_devine_nombre.html')

def webtoona(request):
    return render(request, 'webtoona.html' )


# Create your views here.
