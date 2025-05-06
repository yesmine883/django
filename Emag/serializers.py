from rest_framework.serializers import ModelSerializer 
from Emag.models import Categorie ,Produit
from rest_framework import serializers

class CategorieSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Categorie 
        fields = ['name'] 
class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = ['libelle', 'description', 'prix', 'categorie']