# Generated by Django 2.2.12 on 2020-12-31 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0014_auto_20201223_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolioitem',
            name='address',
        ),
        migrations.RemoveField(
            model_name='portfolioitem',
            name='map_point',
        ),
        migrations.RemoveField(
            model_name='portfolioitem',
            name='porfolio_item_type',
        ),
        migrations.RemoveField(
            model_name='portfolioitem',
            name='progress',
        ),
        migrations.RemoveField(
            model_name='portfolioitem',
            name='worth',
        ),
        migrations.RemoveField(
            model_name='portfolioitem',
            name='year',
        ),
    ]
