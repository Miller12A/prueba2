# Generated by Django 5.0.3 on 2024-04-01 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_rol_rol_opciones_rol_rolopciones_rol_usuarios_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persona',
            old_name='identificaacion',
            new_name='identificacion',
        ),
    ]
