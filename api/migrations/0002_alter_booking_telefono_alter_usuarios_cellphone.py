# Generated by Django 4.0.2 on 2022-03-22 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='telefono',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='cellphone',
            field=models.BigIntegerField(),
        ),
    ]
