# Generated by Django 4.1.6 on 2023-05-30 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_loanding', '0002_delete_stream'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriptiontocourse',
            name='phone_number',
            field=models.CharField(max_length=15, null=True, verbose_name='Номер телефона'),
        ),
    ]