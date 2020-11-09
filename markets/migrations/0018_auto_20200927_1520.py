# Generated by Django 2.2.12 on 2020-09-27 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0017_auto_20200927_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agentleadrequest',
            name='property_type',
            field=models.CharField(choices=[('SINGLEFAMILY', 'Single family'), ('TOWNHOUSE', 'Townhouse'), ('APARTMENT', 'Apartment'), ('TERRACED', 'Terraced house'), ('DORMITORY', 'Dormitory'), ('OTHER', 'Other'), ('BUNGALOW', 'Bungalow'), ('LAND', 'Land'), ('MANSION', 'Mansion'), ('CONDOMINIUM', 'Condominium'), ('DUPLEX', 'Duplex')], max_length=20),
        ),
        migrations.AlterField(
            model_name='agentpropertyrequest',
            name='property_type',
            field=models.CharField(choices=[('SINGLEFAMILY', 'Single family'), ('TOWNHOUSE', 'Townhouse'), ('APARTMENT', 'Apartment'), ('TERRACED', 'Terraced house'), ('DORMITORY', 'Dormitory'), ('OTHER', 'Other'), ('BUNGALOW', 'Bungalow'), ('LAND', 'Land'), ('MANSION', 'Mansion'), ('CONDOMINIUM', 'Condominium'), ('DUPLEX', 'Duplex')], max_length=20),
        ),
        migrations.AlterField(
            model_name='propertyrequestlead',
            name='property_type',
            field=models.CharField(choices=[('SINGLEFAMILY', 'Single family'), ('TOWNHOUSE', 'Townhouse'), ('APARTMENT', 'Apartment'), ('TERRACED', 'Terraced house'), ('DORMITORY', 'Dormitory'), ('OTHER', 'Other'), ('BUNGALOW', 'Bungalow'), ('LAND', 'Land'), ('MANSION', 'Mansion'), ('CONDOMINIUM', 'Condominium'), ('DUPLEX', 'Duplex')], max_length=20),
        ),
    ]