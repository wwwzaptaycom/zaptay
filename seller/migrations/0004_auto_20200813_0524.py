# Generated by Django 3.0.5 on 2020-08-13 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0003_auto_20200808_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='seller_address',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='seller',
            name='seller_specification',
            field=models.CharField(default='', max_length=100),
        ),
    ]
