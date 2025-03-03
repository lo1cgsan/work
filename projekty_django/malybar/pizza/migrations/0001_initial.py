# Generated by Django 5.1.4 on 2025-02-09 18:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=30, verbose_name='Pizza')),
                ('opis', models.TextField(blank=True, help_text='Opis Pizzy')),
                ('rozmiar', models.CharField(choices=[('L', 'duża'), ('M', 'średnia'), ('S', 'mała')], default='L', max_length=1)),
                ('cena', models.DecimalField(decimal_places=2, max_digits=5)),
                ('data', models.DateField(auto_now_add=True, verbose_name='dodano')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'pizze',
            },
        ),
        migrations.CreateModel(
            name='Skladnik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=30, verbose_name='składnik')),
                ('jarski', models.BooleanField(default=False, help_text='Zaznacz, jeżeli składnik jest odpowiedni dla wegetarian', verbose_name='jarski?')),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skladniki', to='pizza.pizza')),
            ],
            options={
                'verbose_name_plural': 'składniki',
            },
        ),
    ]
