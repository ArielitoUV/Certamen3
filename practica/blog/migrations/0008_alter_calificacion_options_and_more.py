# Generated by Django 4.2.7 on 2023-11-29 02:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_calificacion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='calificacion',
            options={'verbose_name': 'Calificacion', 'verbose_name_plural': 'Calificaciones'},
        ),
        migrations.AlterField(
            model_name='calificacion',
            name='calificacion_estrella',
            field=models.PositiveIntegerField(default=1, help_text='Ingrese la calificación estrella del producto (de 1 a 5).', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Calificación del Producto'),
        ),
    ]
