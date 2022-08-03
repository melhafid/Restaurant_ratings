from django import forms
from R_Restaurant_App.models import *
from django.contrib.auth.forms import UserCreationForm

RATINGS_CHOICES = [
    ('0', 0),
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5)
]
class signInForm(forms.Form):
    rating = forms.IntegerField(label="Note", widget=forms.Select(choices=RATINGS_CHOICES))
    comment = forms.CharField(label="Commentaire", max_length=300, required=False)

class CreateUserForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ['username', 'password1', 'password2']