# Generated by Django 3.1.2 on 2020-11-01 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='lat',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='user',
            name='lon',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='user',
            name='occupation',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
