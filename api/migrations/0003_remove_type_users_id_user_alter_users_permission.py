# Generated by Django 4.0.2 on 2022-04-16 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_users_permission'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='type_users',
            name='id_user',
        ),
        migrations.AlterField(
            model_name='users',
            name='permission',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.type_users'),
        ),
    ]
