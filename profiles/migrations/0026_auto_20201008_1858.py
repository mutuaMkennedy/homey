# Generated by Django 2.2.12 on 2020-10-08 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0025_auto_20201008_1801'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicearea',
            old_name='user',
            new_name='created_by',
        ),
        migrations.RenameField(
            model_name='topclient',
            old_name='user',
            new_name='created_by',
        ),
    ]
