# Generated by Django 2.2.12 on 2021-01-19 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0010_auto_20210119_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpostproposal',
            name='job_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_post_proposal', to='markets.JobPost'),
        ),
    ]
