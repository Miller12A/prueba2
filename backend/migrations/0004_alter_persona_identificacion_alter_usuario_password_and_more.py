# Generated by Django 5.0.3 on 2024-04-01 18:28

import backend.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_rename_identificaacion_persona_identificacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='identificacion',
            field=models.CharField(validators=[backend.models.validate_identification]),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(validators=[backend.models.validate_password]),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='user_name',
            field=models.CharField(validators=[backend.models.validate_username]),
        ),
    ]
