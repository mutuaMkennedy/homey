# Generated by Django 2.2.12 on 2021-01-03 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0021_auto_20210103_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessprofile',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
