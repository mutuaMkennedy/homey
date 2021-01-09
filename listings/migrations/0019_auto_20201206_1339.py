# Generated by Django 2.2.12 on 2020-12-06 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0018_auto_20201206_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='type',
            field=models.CharField(choices=[('DUPLEX', 'Duplex'), ('SINGLEFAMILY', 'Single family'), ('TOWNHOUSE', 'Townhouse'), ('TERRACED', 'Terraced house'), ('APARTMENT', 'Apartment'), ('CONDOMINIUM', 'Condominium'), ('MANSION', 'Mansion'), ('OTHER', 'Other'), ('BUNGALOW', 'Bungalow'), ('DORMITORY', 'Dormitory')], default='APARTMENT', max_length=20),
        ),
        migrations.AlterField(
            model_name='propertyopenhouse',
            name='date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='propertyopenhouse',
            name='end_time',
            field=models.TimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='propertyopenhouse',
            name='start_time',
            field=models.TimeField(blank=True, default=None, null=True),
        ),
    ]
