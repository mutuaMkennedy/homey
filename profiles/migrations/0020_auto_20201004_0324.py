# Generated by Django 2.2.12 on 2020-10-04 00:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0019_auto_20201003_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teammate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver_accepted', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=3, null=True)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='join_team_request_receiver', to=settings.AUTH_USER_MODEL)),
                ('requestor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='join_team_requestor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='ProfesionalTeam',
        ),
    ]