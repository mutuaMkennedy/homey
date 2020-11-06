# Generated by Django 2.2.12 on 2020-09-27 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_designandserviceproprojects_project_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pmportfolio',
            name='manager_from',
        ),
        migrations.RemoveField(
            model_name='pmportfolio',
            name='manager_to',
        ),
        migrations.AddField(
            model_name='pmportfolio',
            name='currently_managing',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
