from django.urls import path
from . import views

batalha_pokemon = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    #path('pokemon/', views.PokemonListView.as_view(), name='pokemon-list'),
    # path('pokemon/<int:pk>/', views.PokemonDetailView.as_view(), name='pokemon-detail'),
    # path('trainer/', views.TrainerListView.as_view(), name='trainer-list'),
    # path('trainer/<int:pk>/', views.TrainerDetailView.as_view(), name='trainer-detail'),
]

