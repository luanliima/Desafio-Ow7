from django.db import models
from django.contrib.auth.models import User


class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
class Pokemon(models.Model):
    name = models.CharField(max_length=255)
    attack = models.IntegerField()
    defense = models.IntegerField()
    hp = models.IntegerField()

    def __str__(self):
        return self.name

class trainer(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    name_trainer = models.CharField(max_length=200, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        self.name_trainer = f"{self.name} {self.surname}"
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name

class CampoDeBatalha(models.Model):
    jogador_1 = models.ForeignKey(trainer, on_delete=models.CASCADE, related_name='jogador_1')
    jogador_2 = models.ForeignKey(trainer, on_delete=models.CASCADE, related_name='jogador_2')
    pokemon_jogador_1_1 = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='pokemon_jogador_1_1')
    pokemon_jogador_1_2 = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='pokemon_jogador_1_2')
    pokemon_jogador_1_3 = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='pokemon_jogador_1_3')
    pokemon_jogador_2_1 = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='pokemon_jogador_2_1')
    pokemon_jogador_2_2 = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='pokemon_jogador_2_2')
    pokemon_jogador_2_3 = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='pokemon_jogador_2_3')
    resultado = models.CharField(max_length=255)

    def batalha(self):
        jogador_1_pokemons = [self.pokemon_jogador_1_1, self.pokemon_jogador_1_2, self.pokemon_jogador_1_3]
        jogador_2_pokemons = [self.pokemon_jogador_2_1, self.pokemon_jogador_2_2, self.pokemon_jogador_2_3]

        for i in range(3):
            # Jogador 1 ataca primeiro
            if jogador_1_pokemons[i].ataque > jogador_2_pokemons[i].defesa:
                jogador_2_pokemons[i].hp -= jogador_1_pokemons[i].ataque - jogador_2_pokemons[i].defesa
                if jogador_2_pokemons[i].hp <= 0:
                    self.resultado = f"{self.jogador_1.name} venceu a batalha!"
                    return
            # Jogador 2 ataca em seguida
            else:
                jogador_1_pokemons[i].hp -= jogador_2_pokemons[i].ataque - jogador_1_pokemons[i].defesa
                if jogador_1_pokemons[i].hp <= 0:
                    self.resultado = f"{self.jogador_2.name} venceu a batalha!"
                    return

        if sum(pokemon.hp for pokemon in jogador_1_pokemons) > sum(pokemon.hp for pokemon in jogador_2_pokemons):
            self.resultado = f"{self.jogador_1.name} venceu a batalha!"
        else:
            self.resultado = f"{self.jogador_2.name} venceu a batalha!"



