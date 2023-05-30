from django.urls import path
from . import views
from .views import CategoryAPIView, ProductAPIView
urlpatterns = [
 path('', views.index, name='index'),
 path('listeFournisseur/',views.listFournisseur,name='nouveauFour'),
 path('register/',views.register, name = 'register'),
 path('home/',views.home, name = 'home'),
 path('api/category/', CategoryAPIView.as_view()),
 path('api/produit/', ProductAPIView.as_view()),
]
