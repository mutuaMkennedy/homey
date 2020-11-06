# Generated by Django 2.2.12 on 2020-09-27 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0018_auto_20200927_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agentleadrequest',
            name='property_type',
            field=models.CharField(choices=[('TERRACED', 'Terraced house'), ('TOWNHOUSE', 'Townhouse'), ('MANSION', 'Mansion'), ('DORMITORY', 'Dormitory'), ('DUPLEX', 'Duplex'), ('BUNGALOW', 'Bungalow'), ('CONDOMINIUM', 'Condominium'), ('SINGLEFAMILY', 'Single family'), ('LAND', 'Land'), ('OTHER', 'Other'), ('APARTMENT', 'Apartment')], max_length=20),
        ),
        migrations.AlterField(
            model_name='agentpropertyrequest',
            name='property_type',
            field=models.CharField(choices=[('TERRACED', 'Terraced house'), ('TOWNHOUSE', 'Townhouse'), ('MANSION', 'Mansion'), ('DORMITORY', 'Dormitory'), ('DUPLEX', 'Duplex'), ('BUNGALOW', 'Bungalow'), ('CONDOMINIUM', 'Condominium'), ('SINGLEFAMILY', 'Single family'), ('LAND', 'Land'), ('OTHER', 'Other'), ('APARTMENT', 'Apartment')], max_length=20),
        ),
        migrations.AlterField(
            model_name='propertyrequestlead',
            name='property_type',
            field=models.CharField(choices=[('TERRACED', 'Terraced house'), ('TOWNHOUSE', 'Townhouse'), ('MANSION', 'Mansion'), ('DORMITORY', 'Dormitory'), ('DUPLEX', 'Duplex'), ('BUNGALOW', 'Bungalow'), ('CONDOMINIUM', 'Condominium'), ('SINGLEFAMILY', 'Single family'), ('LAND', 'Land'), ('OTHER', 'Other'), ('APARTMENT', 'Apartment')], max_length=20),
        ),
    ]
