from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from RecipesProject.UsersApp.models import User


class Recipe(models.Model):
    SEASON_CHOICES = [
        ('spring', 'Spring'),
        ('summer', 'Summer'),
        ('autumn', 'Autumn'),
        ('winter', 'Winter')
    ]
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('intermediate', 'Intermediate'),
        ('hard', 'Hard')
    ]
    CATEGORY_CHOICES = [
        ('savory', 'Savory'),
        ('sweet', 'Sweet'),
        ('earthy', 'Earthy'),
        ('spicy', 'Spicy'),
        ('rich', 'Rich')
    ]
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=120, blank=True)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='recipes', null=False, blank=False)
    season = models.CharField(max_length=10, choices=SEASON_CHOICES)
    difficulty = models.CharField(max_length=12, choices=DIFFICULTY_CHOICES)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    ingredients = models.TextField()
    time = models.CharField(max_length=200)
    steps = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("recipe_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        db_table = "recipe"
