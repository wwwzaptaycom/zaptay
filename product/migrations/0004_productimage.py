# Generated by Django 3.0.5 on 2020-08-12 06:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('admin_login', '0002_auto_20200722_1147'),
        ('product', '0003_auto_20200808_1153'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_image_id', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('prod_image_title', models.CharField(max_length=200)),
                ('product_image', models.ImageField(default='', upload_to='products/images')),
                ('product_img_sl_no', models.IntegerField(blank=True, default=0, null=True)),
                ('home_image', models.BooleanField(default=False)),
                ('modify_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_login.zaptayAdmin')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
            ],
            options={
                'db_table': 'product_images',
            },
        ),
    ]