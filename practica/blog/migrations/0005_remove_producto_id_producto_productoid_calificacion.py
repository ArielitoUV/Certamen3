# Generated by Django 4.1 on 2023-11-29 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_cliente_producto_delete_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='id',
        ),
        migrations.AddField(
            model_name='producto',
            name='productoid',
            field=models.CharField(default=1, max_length=50, primary_key=True, serialize=False, verbose_name='ID Producto'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=50, verbose_name='Nombre de producto')),
                ('calificacion_estrella', models.IntegerField(default=0, help_text='Ingrese la calificación estrella del producto (de 1 a 5).', verbose_name='Calificación Estrella')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.producto', verbose_name='Producto')),
            ],
            options={
                'verbose_name': 'Calificacion',
                'verbose_name_plural': 'Calificacion',
            },
        ),
    ]
