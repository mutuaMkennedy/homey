# Generated by Django 2.2.12 on 2021-01-28 09:13

import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0022_businessprofile_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessprofile',
            name='address',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='businessprofile',
            name='business_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='businessprofile',
            name='facebook_page_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='businessprofile',
            name='instagram_page_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='businessprofile',
            name='linkedin_page_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='businessprofile',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
        migrations.AlterField(
            model_name='businessprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='businessprofile',
            name='service_areas',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100, null=True), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='businessprofile',
            name='twitter_page_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='businessprofile',
            name='website_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
