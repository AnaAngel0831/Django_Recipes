from .models import Drinks
from django import forms


class DrinksForm(forms.ModelForm):

    title = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 1}))
    image = forms.ImageField(required=True)
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    season = forms.TypedChoiceField(choices=Drinks.SEASON_CHOICES, coerce=str, required=True,
                                    widget=forms.Select(attrs={'class': 'form-control'}))
    difficulty = forms.TypedChoiceField(choices=Drinks.DIFFICULTY_CHOICES, coerce=str, required=True,
                                        widget=forms.Select(attrs={'class': 'form-control'}))
    category = forms.TypedChoiceField(choices=Drinks.CATEGORY_CHOICES, required=True,
                                      widget=forms.Select(attrs={'class': 'form-control'}))
    ingredients = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 6}))
    time = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 1}))
    steps = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 10}))

    class Meta:
        model = Drinks
        fields = ("title", "slug", "image", "description", "difficulty", "season", "category", "ingredients", "time",
                  "steps")

