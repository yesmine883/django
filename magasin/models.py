from django.db import models
from datetime import date
# Create your models here.s
class Produit(models.Model):
    TYPE_CHOICES = [
        ('em', 'Emballé'),
        ('fr', 'Frais'),
        ('cs', 'Conserve'),
    ]

    libelle = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=3)
    typeProduit = models.CharField(max_length=2, choices=TYPE_CHOICES, default='em')
    image=models.ImageField (blank=True )
    Categorie=models.ForeignKey('Categorie',on_delete=models.CASCADE, null=True , blank=True)
    Fournisseur=models.ForeignKey('Fournisseur',on_delete=models.CASCADE, null=True  )
    def __str__(self):
        return self.libelle+str(self.prix)
    
    
class Categorie (models.Model):
    name=models.CharField(max_length=50, default='Alimentaire')
    def __str__(self):
        return self.name
    

class Fournisseur  (models.Model):
        nom=models.CharField(max_length=100)
        adresse=models.TextField()
        email=models.EmailField()
        telephone=models.CharField( max_length=8)
        def __str__(self):
            return self.nom
        
        
class  ProduitNC (Produit):
    Duree_garantie=models.CharField( max_length=100)
    def __str__(self):
            return self.Duree_garantie
        
        
class Commande (models.Model):
   dateCde = models.DateField( null=True,  default=date.today)
   totalCde =models.DecimalField(max_digits=10,decimal_places=3 )
   Produit=models.ManyToManyField('Produit')
   def __str__(self):
            return str(self.dateCde) 
    
        

