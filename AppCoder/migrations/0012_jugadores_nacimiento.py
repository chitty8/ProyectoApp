# Generated by Django 4.1.2 on 2022-11-16 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0011_jugadores_equipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='jugadores',
            name='nacimiento',
            field=models.DateField(null=True),
        ),
    ]