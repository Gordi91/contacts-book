from django.contrib import admin
from contacts_book import models


class PersonInline(admin.TabularInline):
    model = models.Person.groups.through


@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    filter_horizontal = ('groups',)


@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    inlines = [
        PersonInline,
    ]


@admin.register(models.Email)
class EmailAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Phone)
class PhoneAdmin(admin.ModelAdmin):
    pass



