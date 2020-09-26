# Generated by Django 3.0.5 on 2020-09-25 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stock', '__first__'),
        ('product', '0001_initial'),
        ('admin_login', '0002_auto_20200722_1147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_custom_id', models.CharField(blank=True, max_length=150, null=True, unique=True)),
                ('offer_title', models.CharField(max_length=250)),
                ('offer_start', models.DateTimeField()),
                ('offer_end', models.DateTimeField()),
                ('offer_status', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_login.zaptayAdmin')),
            ],
            options={
                'db_table': 'offers',
            },
        ),
        migrations.CreateModel(
            name='OfferProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_product_id', models.CharField(blank=True, max_length=150, null=True, unique=True)),
                ('extra_offer_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_login.zaptayAdmin')),
                ('bach_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stock.Bach')),
                ('offer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offer.Offer')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
            ],
            options={
                'db_table': 'offer_products',
            },
        ),
    ]
