from django.shortcuts import render
from django.template import loader
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    context = {'val': "Menu Accueil"}
    return render(request, 'home.html', context)

def index(request):
 return render(request,'acceuil.html' )