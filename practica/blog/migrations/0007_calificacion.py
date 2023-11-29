# Generated by Django 4.1 on 2023-11-29 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_delete_calificacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Reseña')),
                ('calificacion_estrella', models.IntegerField(default=0, help_text='Ingrese la calificación estrella del producto (de 1 a 5).', verbose_name='Calificación Estrella')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.producto', verbose_name='Nombre Producto')),
            ],
            options={
                'verbose_name': 'Calificacion',
                'verbose_name_plural': 'Calificacion',
            },
        ),
    ]
