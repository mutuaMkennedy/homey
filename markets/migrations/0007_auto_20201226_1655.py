# Generated by Django 2.2.12 on 2020-12-26 13:55

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0006_auto_20201225_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='location',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='project_duration',
            field=models.CharField(choices=[('1', '<span>less than a week</span>'), ('2', '<span>less than 1 month</span>'), ('4', '<span>1 to 3 months</span>'), ('5', '<span>3 to 6 months</span>'), ('6', '<span>more than 6 months</span>')], max_length=20),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='project_size',
            field=models.CharField(choices=[('LARGE', '<span>Large</span> <small>Mostly a longer term activity with a series of complex multiple requirements.<br>Example: Designing and building a house. </small>'), ('MEDIUM', '<span>Medium</span><small> A moderately complex activity with a well defined time frame.<br>Example: Home value assessment. </small>'), ('SMALL', '<span>Small</span> <small>A relatively quick activity with less complex steps which can ussually be done in a small time frame.<br>Examples: Cleaning service, Moving service etc. </small>')], max_length=20),
        ),
    ]