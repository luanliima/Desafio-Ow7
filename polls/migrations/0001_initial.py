# Generated by Django 4.1.7 on 2023-03-28 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('attack', models.IntegerField()),
                ('defense', models.IntegerField()),
                ('hp', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Treinador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sobrenome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('nome_treinador', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.poll')),
            ],
        ),
        migrations.CreateModel(
            name='CampoDeBatalha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resultado', models.CharField(max_length=255)),
                ('jogador_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jogador_1', to='polls.treinador')),
                ('jogador_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jogador_2', to='polls.treinador')),
                ('pokemon_jogador_1_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pokemon_jogador_1_1', to='polls.pokemon')),
                ('pokemon_jogador_1_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pokemon_jogador_1_2', to='polls.pokemon')),
                ('pokemon_jogador_1_3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pokemon_jogador_1_3', to='polls.pokemon')),
                ('pokemon_jogador_2_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pokemon_jogador_2_1', to='polls.pokemon')),
                ('pokemon_jogador_2_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pokemon_jogador_2_2', to='polls.pokemon')),
                ('pokemon_jogador_2_3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pokemon_jogador_2_3', to='polls.pokemon')),
            ],
        ),
    ]