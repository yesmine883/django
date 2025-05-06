from rest_framework import routers 
from .views import CategorieViewSet ,ProduitViewSet
from django.urls import path, include 
router = routers.DefaultRouter() 
router.register('categorie', CategorieViewSet, basename='categorie') 
router.register('produit', ProduitViewSet, basename='produit') 
urlpatterns = router.urls 