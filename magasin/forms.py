from django.forms import ModelForm
from .models import Produit
from .models import Commande
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')


class ProduitForm(ModelForm):
    class Meta:
        model = Produit
        fields = "__all__"  # ou fields = ['libelle', 'description']
class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['dateCde', 'totalCde', 'Produit']
        widgets = {
            'Produit': forms.CheckboxSelectMultiple(),  # permet de cocher plusieurs produits
            'dateCde': forms.DateInput(attrs={'type': 'date'})
        }

