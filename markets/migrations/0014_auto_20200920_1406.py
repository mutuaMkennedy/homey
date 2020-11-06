# Generated by Django 2.2.12 on 2020-09-20 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0013_auto_20200920_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agentleadrequest',
            name='property_type',
            field=models.CharField(choices=[('BUNGALOW', 'Bungalow'), ('TERRACED', 'Terraced house'), ('OTHER', 'Other'), ('DUPLEX', 'Duplex'), ('TOWNHOUSE', 'Townhouse'), ('LAND', 'Land'), ('MANSION', 'Mansion'), ('SINGLEFAMILY', 'Single family'), ('CONDOMINIUM', 'Condominium'), ('APARTMENT', 'Apartment'), ('DORMITORY', 'Dormitory')], max_length=20),
        ),
        migrations.AlterField(
            model_name='agentpropertyrequest',
            name='property_type',
            field=models.CharField(choices=[('BUNGALOW', 'Bungalow'), ('TERRACED', 'Terraced house'), ('OTHER', 'Other'), ('DUPLEX', 'Duplex'), ('TOWNHOUSE', 'Townhouse'), ('LAND', 'Land'), ('MANSION', 'Mansion'), ('SINGLEFAMILY', 'Single family'), ('CONDOMINIUM', 'Condominium'), ('APARTMENT', 'Apartment'), ('DORMITORY', 'Dormitory')], max_length=20),
        ),
        migrations.AlterField(
            model_name='propertyrequestlead',
            name='property_type',
            field=models.CharField(choices=[('BUNGALOW', 'Bungalow'), ('TERRACED', 'Terraced house'), ('OTHER', 'Other'), ('DUPLEX', 'Duplex'), ('TOWNHOUSE', 'Townhouse'), ('LAND', 'Land'), ('MANSION', 'Mansion'), ('SINGLEFAMILY', 'Single family'), ('CONDOMINIUM', 'Condominium'), ('APARTMENT', 'Apartment'), ('DORMITORY', 'Dormitory')], max_length=20),
        ),
    ]
