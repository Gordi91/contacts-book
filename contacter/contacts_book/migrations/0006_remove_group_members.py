# Generated by Django 2.1.4 on 2019-01-11 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts_book', '0005_person_groups'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='members',
        ),
    ]
