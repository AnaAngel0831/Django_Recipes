from .models import Recipe
from django import forms


class RecipeForm(forms.ModelForm):

    title = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 1}))
    image = forms.ImageField(required=True)
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    season = forms.TypedChoiceField(choices=Recipe.SEASON_CHOICES, coerce=str, required=True,
                                    widget=forms.Select(attrs={'class': 'form-control'}))
    difficulty = forms.TypedChoiceField(choices=Recipe.DIFFICULTY_CHOICES, coerce=str, required=True,
                                        widget=forms.Select(attrs={'class': 'form-control'}))
    category = forms.TypedChoiceField(choices=Recipe.CATEGORY_CHOICES, required=True,
                                      widget=forms.Select(attrs={'class': 'form-control'}))
    ingredients = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 6}))
    time = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 1}))
    steps = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 10}))

    class Meta:
        model = Recipe
        fields = ("title", "image", "description", "difficulty", "season", "category", "ingredients", "time", "steps")
