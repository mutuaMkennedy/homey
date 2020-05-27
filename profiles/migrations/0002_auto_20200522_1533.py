# Generated by Django 2.2.12 on 2020-05-22 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('NormalUser', 'Normaluser'), ('Agent', 'Agent'), ('PropertyManager', 'PropertyManager'), ('Design&servicePro', 'Design&servicePro'), ('Admin', 'Admin')], default='NormalUser', max_length=10),
        ),
    ]
