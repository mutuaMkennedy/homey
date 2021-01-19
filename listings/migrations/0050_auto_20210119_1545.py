# Generated by Django 2.2.12 on 2021-01-19 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0049_auto_20210119_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='type',
            field=models.CharField(choices=[('SINGLEFAMILY', 'Single family'), ('CONDOMINIUM', 'Condominium'), ('DORMITORY', 'Dormitory'), ('MANSION', 'Mansion'), ('APARTMENT', 'Apartment'), ('BUNGALOW', 'Bungalow'), ('TOWNHOUSE', 'Townhouse'), ('OTHER', 'Other'), ('DUPLEX', 'Duplex'), ('TERRACED', 'Terraced house')], default='APARTMENT', max_length=20),
        ),
    ]
