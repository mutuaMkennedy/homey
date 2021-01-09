# Generated by Django 2.2.12 on 2021-01-02 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0032_auto_20210102_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='type',
            field=models.CharField(choices=[('APARTMENT', 'Apartment'), ('DORMITORY', 'Dormitory'), ('CONDOMINIUM', 'Condominium'), ('TERRACED', 'Terraced house'), ('MANSION', 'Mansion'), ('TOWNHOUSE', 'Townhouse'), ('OTHER', 'Other'), ('BUNGALOW', 'Bungalow'), ('SINGLEFAMILY', 'Single family'), ('DUPLEX', 'Duplex')], default='APARTMENT', max_length=20),
        ),
    ]
