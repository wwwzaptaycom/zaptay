# Generated by Django 3.0.5 on 2020-09-25 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attribute', '0008_undertertiarycategory'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prod_brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attribute.Brand'),
        ),
    ]
