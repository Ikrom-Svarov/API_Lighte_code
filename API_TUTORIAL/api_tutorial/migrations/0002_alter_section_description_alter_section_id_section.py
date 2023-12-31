# Generated by Django 4.1.6 on 2023-07-14 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_tutorial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='description',
            field=models.TextField(null=True, verbose_name='Описание для подраздела'),
        ),
        migrations.AlterField(
            model_name='section',
            name='id_section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='api_tutorial.section'),
        ),
    ]
