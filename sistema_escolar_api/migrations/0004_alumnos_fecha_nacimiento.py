# Generated by Django 5.0.2 on 2025-03-12 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_escolar_api', '0003_alumnos'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumnos',
            name='fecha_nacimiento',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
