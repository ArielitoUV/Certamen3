# Generated by Django 4.1 on 2023-11-29 01:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_producto_id_producto_productoid_calificacion'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Calificacion',
        ),
    ]
