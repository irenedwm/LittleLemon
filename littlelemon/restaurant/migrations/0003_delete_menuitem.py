# Generated by Django 4.2 on 2023-05-02 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_menuitem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MenuItem',
        ),
    ]
