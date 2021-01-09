# Generated by Django 2.2.12 on 2021-01-02 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0017_auto_20210102_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessprofile',
            name='professional_category',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pro_business_category', to='profiles.ProfessionalCategory'),
        ),
        migrations.AlterField(
            model_name='professionalcategory',
            name='professional_group',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='pro_category_group', to='profiles.ProfessionalGroup'),
        ),
    ]
