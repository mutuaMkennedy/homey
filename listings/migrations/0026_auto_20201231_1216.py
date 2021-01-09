# Generated by Django 2.2.12 on 2020-12-31 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0025_auto_20201220_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='type',
            field=models.CharField(choices=[('DORMITORY', 'Dormitory'), ('CONDOMINIUM', 'Condominium'), ('MANSION', 'Mansion'), ('TOWNHOUSE', 'Townhouse'), ('DUPLEX', 'Duplex'), ('SINGLEFAMILY', 'Single family'), ('TERRACED', 'Terraced house'), ('OTHER', 'Other'), ('BUNGALOW', 'Bungalow'), ('APARTMENT', 'Apartment')], default='APARTMENT', max_length=20),
        ),
    ]
