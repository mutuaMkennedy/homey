# Generated by Django 2.2.12 on 2021-01-22 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0053_auto_20210121_1259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='type',
        ),
    ]
