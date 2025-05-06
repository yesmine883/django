from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('categorie/<str:cat_name>/', views.produits_par_categorie, name='produits_par_categorie'),
    path('vitrine/', views.vitrine, name='vitrine'),
    path('commande/', views.commande, name='commande'),
    path('register/', views.register, name='register'),
    path('', views.index, name='acceuil'), 
    path('maj/', views.maj_produits, name='maj_produits'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
