# Generated by Django 4.1.2 on 2022-11-09 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0006_entregables_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='entregables',
            name='estudiante',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AppCoder.estudiantes'),
        ),
    ]