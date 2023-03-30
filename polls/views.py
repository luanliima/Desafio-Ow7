from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Pokemon, trainer
#from .forms import TrainerForm, PokemonForm


def index(request):
    trainers = trainer.objects.all()
    context = {'trainers': trainers}
    return render(request, 'polls/index.html', context)


def trainer_detail(request, trainer_id):
    trainer = get_object_or_404(trainer, pk=trainer_id)
    context = {'trainer': trainer}
    return render(request, 'polls/trainer_detail.html', context)


# def trainer_create(request):
#     if request.method == 'POST':
#         form = TrainerForm(request.POST)
#         if form.is_valid():
#             trainer = form.save()
#        return HttpResponseRedirect(reverse('polls:trainer_detail', args=[trainer.id]))
#     else:
#         form = TrainerForm()
#     context = {'form': form}
#     return render(request, 'polls/trainer_form.html', context)


def pokemon_detail(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, pk=pokemon_id)
    context = {'pokemon': pokemon}
    return render(request, 'polls/pokemon_detail.html', context)


# def pokemon_create(request):
#     if request.method == 'POST':
#         form = PokemonForm(request.POST)
#         if form.is_valid():
#             pokemon = form.save()
#             return HttpResponseRedirect(reverse('polls:pokemon_detail', args=[pokemon.id]))
#     else:
#         form = PokemonForm()
#     context = {'form': form}
#     return render(request, 'polls/pokemon_form.html', context)


def battle(request, trainer1_id, trainer2_id):
    trainer1 = get_object_or_404(trainer, pk=trainer1_id)
    trainer2 = get_object_or_404(trainer, pk=trainer2_id)
    context = {'trainer1': trainer1, 'trainer2': trainer2}
    return render(request, 'polls/battle.html', context)


