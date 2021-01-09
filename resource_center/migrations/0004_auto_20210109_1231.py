# Generated by Django 2.2.12 on 2021-01-09 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resource_center', '0003_auto_20210108_2053'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='blogpost',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='blog_category',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blog_post_category', to='resource_center.BlogCategory'),
        ),
    ]
