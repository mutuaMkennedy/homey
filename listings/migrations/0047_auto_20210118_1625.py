# Generated by Django 2.2.12 on 2021-01-18 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0046_auto_20210118_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='type',
            field=models.CharField(choices=[('OTHER', 'Other'), ('DORMITORY', 'Dormitory'), ('BUNGALOW', 'Bungalow'), ('CONDOMINIUM', 'Condominium'), ('MANSION', 'Mansion'), ('TERRACED', 'Terraced house'), ('SINGLEFAMILY', 'Single family'), ('DUPLEX', 'Duplex'), ('TOWNHOUSE', 'Townhouse'), ('APARTMENT', 'Apartment')], default='APARTMENT', max_length=20),
        ),
    ]