# Generated by Django 3.0.5 on 2020-09-12 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attribute', '0005_subcategory_sub_category_seo_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='tertiarycategory',
            name='ter_category_seo_url',
            field=models.CharField(default='', max_length=255),
        ),
    ]