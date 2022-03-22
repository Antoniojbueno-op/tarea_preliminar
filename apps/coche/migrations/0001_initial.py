# Generated by Django 4.0.2 on 2022-03-16 10:33

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coche',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, null=True)),
                ('Telefono', phone_field.models.PhoneField(blank=True, max_length=31, null=True)),
                ('matricula', models.CharField(max_length=7, unique=True, verbose_name='Matricula')),
            ],
        ),
    ]
