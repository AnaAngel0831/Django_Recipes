# Generated by Django 4.1.6 on 2023-09-27 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=120, unique=True)),
                ('description', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='recipes')),
                ('season', models.CharField(choices=[('spring', 'Spring'), ('summer', 'Summer'), ('autumn', 'Autumn'), ('winter', 'Winter')], max_length=10)),
                ('difficulty', models.CharField(choices=[('easy', 'Easy'), ('intermediate', 'Intermediate'), ('hard', 'Hard')], max_length=12)),
                ('category', models.CharField(choices=[('savory', 'Savory'), ('sweet', 'Sweet'), ('earthy', 'Earthy'), ('spicy', 'Spicy'), ('rich', 'Rich')], max_length=10)),
                ('ingredients', models.TextField()),
                ('time', models.CharField(max_length=200)),
                ('steps', models.TextField()),
            ],
            options={
                'db_table': 'recipe',
            },
        ),
        migrations.CreateModel(
            name='RecipeDetailView',
            fields=[
                ('recipe_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='RecipesApp.recipe')),
            ],
            bases=('RecipesApp.recipe',),
        ),
    ]
