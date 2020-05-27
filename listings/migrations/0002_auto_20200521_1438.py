# Generated by Django 2.2.12 on 2020-05-21 11:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('listings', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='rentalproperty',
            name='favourite',
            field=models.ManyToManyField(blank=True, related_name='rental_favourite', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rentalproperty',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='rent_property', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rentalimages',
            name='property',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='listings.RentalProperty'),
        ),
        migrations.AddField(
            model_name='propertyforsalevideos',
            name='property',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='listings.PropertyForSale'),
        ),
        migrations.AddField(
            model_name='propertyforsaleimages',
            name='property',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='listings.PropertyForSale'),
        ),
        migrations.AddField(
            model_name='propertyforsale',
            name='favourite',
            field=models.ManyToManyField(blank=True, related_name='favourite', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='propertyforsale',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='sale_property', to=settings.AUTH_USER_MODEL),
        ),
    ]
