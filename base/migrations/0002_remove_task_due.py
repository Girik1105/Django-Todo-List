# Generated by Django 3.1.5 on 2021-03-22 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='due',
        ),
    ]
