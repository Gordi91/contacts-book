from django.db import models
from django.core.validators import RegexValidator


class Address(models.Model):
    town = models.CharField(max_length=120, verbose_name="Town")
    street = models.CharField(max_length=120, verbose_name="Street")
    house_number = models.PositiveSmallIntegerField(verbose_name="House number")
    apartment_number = models.PositiveSmallIntegerField(verbose_name="Apartment number", null=True, blank=True)

    def __str__(self):
        return f"{self.street} {self.house_number}/{self.apartment_number}, {self.town}"


class Person(models.Model):
    first_name = models.CharField(max_length=120, verbose_name="First name")
    surname = models.CharField(max_length=120, verbose_name="Surname")
    description = models.TextField(verbose_name="Description")
    address = models.ForeignKey(Address, verbose_name="Address", on_delete=models.DO_NOTHING, null=True, blank=True)
    avatar = models.ImageField(upload_to='images/avatars')
    groups = models.ManyToManyField('contacts_book.Group', verbose_name="Groups", blank=True)

    def __str__(self):
        return f"{self.first_name} {self.surname}"

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "People"
        ordering = ['surname', 'first_name']


PHONE_TYPES = (
    (1, 'Cellphone'),
    (2, 'Home'),
    (3, 'Work'),
)

EMAIL_CHOICES = (
    (1, 'Home'),
    (2, 'Work'),
)


class Phone(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?\d{2}? ?(\d{3}?(-| )?){3}$',
                                 message="Phone number format: '+## ### ### ###'")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, verbose_name="Phone number")
    phone_type = models.PositiveSmallIntegerField(
        choices=PHONE_TYPES,
        verbose_name="Phone type"
    )
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name="Person")

    def __str__(self):
        return f"{self.phone_number} {self.person}"


class Email(models.Model):
    email_address = models.EmailField(unique=True, verbose_name="Email address")
    email_type = models.PositiveSmallIntegerField(
        choices=EMAIL_CHOICES,
        verbose_name="Email type",
    )
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.email_address


class Group(models.Model):
    name = models.CharField(max_length=64, verbose_name="Group name")


    def __str__(self):
        return self.name
