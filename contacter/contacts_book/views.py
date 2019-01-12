from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Person, Address, Group, Phone, Email
from .forms import PersonForm, AddressForm, PhoneForm, EmailForm, GroupForm, MembersForm



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
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            person_id = form.instance.id
        return redirect('show_person', id=person_id)


class ModifyPerson(View):

    def get(self, request, id):
        template_name = 'contacts_book/new_person.html'
        person = get_object_or_404(Person, pk=id)
        form = PersonForm(initial={
            'first_name': person.first_name,
            'surname': person.surname,
            'description': person.description,
            'avatar': person.avatar,
            'groups': [group.id for group in person.groups.all()],
        })

        return render(request, template_name, {
            'form': form,
            'person': person,
        })

    def post(self, request, id):
        instance = get_object_or_404(Person, pk=id)
        form = PersonForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
        return redirect('show_person', id=id)


class ShowPerson(View):
    def get(self, request, id):
        template_name = 'contacts_book/show_person.html'
        person = Person.objects.get(pk=id)
        phones = Phone.objects.filter(person=person)
        emails = Email.objects.filter(person=person)
        return render(request, template_name, {
            'person': person,
            'phones': phones,
            'emails': emails,
        })


class AddAddress(View):
    def get(self, request, id):
        template_name = 'contacts_book/add_address.html'
        person = Person.objects.get(pk=id)

        if Address.objects.filter(person=person):
            address = Address.objects.filter(person=person)[0]
            form = AddressForm(initial={
                'town': address.town,
                'street': address.street,
                'house_number': address.house_number,
                'apartment_number': address.apartment_number,
            })
        else:
            form = AddressForm()

        return render(request, template_name, {
            'form': form,
        })

    def post(self, request, id):
        form = AddressForm(request.POST)

        if form.is_valid():
            form.save()
            address = Address.objects.get(pk=form.instance.id)
            person = get_object_or_404(Person, pk=id)
            person.address = address
            person.save()
        return redirect('modify_person', id=id)


class AddPhoneNumber(View):
    def get(self, request, id):
        template_name = 'contacts_book/add_phone_number.html'
        form = PhoneForm()
        return render(request, template_name, {
            'form': form,
        })

    def post(self, request, id):
        form = PhoneForm(request.POST)
        person = get_object_or_404(Person, pk=id)
        form.save(commit=False)
        if form.is_valid:
            obj = form.save(commit=False)
            obj.person = person
            obj.save()
        return redirect('modify_person', id=id)


class AddEMail(View):
    def get(self, request, id):
        template_name = 'contacts_book/add_email.html'
        form = EmailForm()
        return render(request, template_name, {
            'form': form,
        })

    def post(self, request, id):
        form = EmailForm(request.POST)
        person = get_object_or_404(Person, pk=id)
        if form.is_valid:
            obj = form.save(commit=False)
            obj.person = person
            obj.save()
        return redirect('modify_person', id=id)


class NewGroup(View):
    def get(self, request):
        template_name = 'contacts_book/new_group.html'
        form = GroupForm()
        return render(request, template_name, {
            'form': form,
        })

    def post(self, request):
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            group_id = form.instance.id
        return redirect('show_group', id=group_id)


class ModifyGroup(View):
    def get(self, request, id):
        template_name = 'contacts_book/new_group.html'
        group = get_object_or_404(Group, pk=id)
        form = GroupForm(initial={
            'name': group.name,
        })

        return render(request, template_name, {
            'form': form,
            'group_id': group.id,
        })

    def post(self, request, id):
        instance = get_object_or_404(Group, pk=id)
        form = GroupForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
        return redirect('show_group', id=id)


class ShowGroups(View):
    def get(self, request):
        template_name = 'contacts_book/show_groups.html'
        groups = Group.objects.all()
        return render(request, template_name, {'groups': groups})

    def post(self, request):
        template_name = 'contacts_book/show_groups.html'
        groups = Group.objects.all()
        if request.POST.get('surname'):
            surname = request.POST.get('surname')
            groups = groups.filter(person__surname__icontains=surname)
        message = ''
        if not groups.exists():
            message = "No groups found for given search criteria"
        return render(request, template_name, {
            'groups': groups,
            'message': message,
        })


class ShowGroup(View):
    def get(self, request, id):
        template_name = 'contacts_book/show_group.html'
        group = Group.objects.get(pk=id)
        return render(request, template_name, {'group': group})


class DeletePersonFromGroup(View):
    def get(self, request, group_id, person_id):
        person = get_object_or_404(Person, pk=person_id)
        person.groups.remove(Group.objects.get(pk=group_id))
        return redirect('show_group', id=group_id)


class DeleteGroup(View):
    def get(self, request, id):
        Group.objects.get(pk=id).delete()
        return redirect('show_groups')


class GroupMembers(View):
    def get(self, request, id):
        template_name = 'contacts_book/group_members.html'
        group = Group.objects.get(pk=id)
        members_form = MembersForm(initial={
            'members': [person.id for person in group.person_set.all()],
        })
        return render(request, template_name, {
            'members_form': members_form,
            'group': group,
        })

    def post(self, request, id):
        group = Group.objects.get(pk=id)
        members = request.POST.getlist('members')
        for person_id in members:
            Person.objects.get(pk=person_id).groups.add(group)
        return redirect('show_group', id=id)


class DeleteEmailFromPerson(View):
    def get(self, request, email_id, person_id):
        get_object_or_404(Email, pk=email_id).delete()
        return redirect('modify_person', id=person_id)


class DeletePhoneFromPerson(View):
    def get(self, request, phone_id, person_id):
        get_object_or_404(Phone, pk=phone_id).delete()
        return redirect('modify_person', id=person_id)
