from django.db import models

# Create your models here.
class Produit(models.Model):
    libelle = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=3)
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.libelle} - {self.description[:30]}... - {self.prix}€ - Categorie: {self.categorie.name if self.categorie else "Aucune"}'

class Categorie (models.Model):
    name=models.CharField(max_length=50, default='Alimentaire')
    def __str__(self):
        return self.name