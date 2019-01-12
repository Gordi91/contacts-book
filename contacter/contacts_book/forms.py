from django import forms
from contacts_book import models


class PersonForm(forms.ModelForm):
    class Meta:
        model = models.Person
        exclude = ['id', 'address']


class AddressForm(forms.ModelForm):
    class Meta:
        model = models.Address
        exclude = ['id']


class PhoneForm(forms.ModelForm):
    class Meta:
        model = models.Phone
        exclude = ['id', 'person']


class EmailForm(forms.ModelForm):
    class Meta:
        model = models.Email
        exclude = ['id', 'person']


class GroupForm(forms.ModelForm):
    class Meta:
        model = models.Group
        exclude = ['id']


class MembersForm(forms.Form):
        members = forms.MultipleChoiceField(
            required=False,
            widget=forms.CheckboxSelectMultiple,
            choices=[(person.id, f'{person.first_name} {person.surname}') for person in models.Person.objects.all()],
        )
