# Generated by Django 4.1.6 on 2023-06-09 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_srm', '0002_lead_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
