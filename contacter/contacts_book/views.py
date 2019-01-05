from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Person, Address, Group, Phone
from .forms import PersonForm


class ShowPeople(View):
    def get(self, request):
        template_name = 'contacts_book/show_people.html'
        people = Person.objects.all()
        return render(request, template_name, {'people': people})


class DeletePerson(View):
    def get(self, request, id):
        Person.objects.get(pk=id).delete()
        return redirect('show_people')


class NewPerson(View):
    def get(self, request):
        template_name = 'contacts_book/new_person.html'
        form = PersonForm()
        return render(request, template_name, {
            'form': form,
        })

    def post(self, request):
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Something went wrong")
            # print(form)
        return redirect('show_people')


class ModifyPerson(View):
    def get(self, request, id):
        template_name = 'contacts_book/new_person.html'
        person = Person.objects.get(pk=id)
        form = PersonForm(initial={
            'first_name': person.first_name,
            'surname': person.surname,
            'description': person.description,
            'address': person.address,
            'avatar': person.avatar,
            'groups': [group.id for group in person.groups.all()],
        })

        return render(request, template_name, {
            'form': form,
        })

    def post(self, request, id):
        instance = get_object_or_404(Person, pk=id)
        form = PersonForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
        return redirect('show_people')
