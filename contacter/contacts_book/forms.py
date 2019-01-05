from django import forms
from contacts_book import models


class PersonForm(forms.ModelForm):
    class Meta:
        model = models.Person
        exclude = ['id']
