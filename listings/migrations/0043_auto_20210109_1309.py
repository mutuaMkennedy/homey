# Generated by Django 2.2.12 on 2021-01-09 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0042_auto_20210109_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='type',
            field=models.CharField(choices=[('DUPLEX', 'Duplex'), ('TERRACED', 'Terraced house'), ('OTHER', 'Other'), ('MANSION', 'Mansion'), ('APARTMENT', 'Apartment'), ('DORMITORY', 'Dormitory'), ('BUNGALOW', 'Bungalow'), ('SINGLEFAMILY', 'Single family'), ('CONDOMINIUM', 'Condominium'), ('TOWNHOUSE', 'Townhouse')], default='APARTMENT', max_length=20),
        ),
    ]
