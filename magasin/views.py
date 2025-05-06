from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Produit, Categorie
from .forms import ProduitForm  # from forms.py (not formulaire.py anymore)
from .forms import CommandeForm
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
                return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

# Default catalog page
def index(request):
    products = Produit.objects.all()
    context = {'products': products}
    return render(request, 'magasin/mesProduits.html', context)

# Filter products by category name
def produits_par_categorie(request, cat_name):
    category = get_object_or_404(Categorie, name=cat_name)
    products = Produit.objects.filter(Categorie=category)
    return render(request, 'magasin/mesProduits.html', {'products': products})

# Product form + display: alternative view (different route)
def admin_required(view_func):
    decorated_view_func = user_passes_test(lambda user: user.is_authenticated and user.is_superuser)(view_func)
    return decorated_view_func

def vitrine(request):
    produits = Produit.objects.all()
    return render(request, 'magasin/vitrine.html', {'list': produits})

def commande(request):
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('commande')  # Recharge la page
    else:
        form = CommandeForm()
    return render(request, 'magasin/commande.html', {'form': form})



def maj_produits(request):
    print(">>> maj_produits appelée")  
    if request.method == "POST":
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('maj_produits')  
    else:
        form = ProduitForm()
    return render(request, 'magasin/majProduits.html', {'form': form})