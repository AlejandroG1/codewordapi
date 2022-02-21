# Generated by Django 4.0.2 on 2022-02-15 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='restaurantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_restaurant', models.CharField(max_length=50)),
                ('type_table_1', models.CharField(max_length=50)),
                ('type_table_2', models.CharField(max_length=50)),
                ('type_table_3', models.CharField(max_length=50)),
                ('name_menu', models.CharField(max_length=50)),
                ('saucer_1', models.CharField(max_length=50)),
                ('saucer_2', models.CharField(max_length=50)),
                ('saucer_3', models.CharField(max_length=50)),
                ('phone', models.PositiveIntegerField()),
                ('address', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='usuarios',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('contactmail', models.CharField(max_length=30)),
                ('cellphone', models.PositiveIntegerField()),
            ],
        ),
    ]
