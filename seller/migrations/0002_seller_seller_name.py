# Generated by Django 3.0.5 on 2020-08-08 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='seller_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
