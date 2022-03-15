# Generated by Django 4.0.2 on 2022-03-15 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='restaurantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_restaurant', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=1024)),
                ('restaurant_image', models.ImageField(blank=True, upload_to='media', verbose_name='view')),
            ],
        ),
        migrations.CreateModel(
            name='usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('contactmail', models.CharField(max_length=30)),
                ('cellphone', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='promociones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_promocion', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=1024)),
                ('promocion_image', models.ImageField(blank=True, upload_to='media', verbose_name='view')),
                ('restaurante_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.restaurantes')),
            ],
        ),
        migrations.CreateModel(
            name='menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_platillo', models.CharField(max_length=100)),
                ('ingredientes', models.CharField(max_length=1024)),
                ('restaurante_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.restaurantes')),
            ],
        ),
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=50)),
                ('apellido_usuario', models.CharField(max_length=50)),
                ('telefono', models.PositiveIntegerField()),
                ('email', models.CharField(max_length=30)),
                ('dia_hora_booking', models.DateTimeField()),
                ('solicitud_especial', models.CharField(max_length=1024)),
                ('number_people', models.PositiveIntegerField()),
                ('restaurante_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.restaurantes')),
            ],
        ),
    ]
