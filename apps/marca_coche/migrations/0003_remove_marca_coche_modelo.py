# Generated by Django 4.0.2 on 2022-03-18 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marca_coche', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marca_coche',
            name='modelo',
        ),
    ]