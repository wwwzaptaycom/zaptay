# Generated by Django 3.0.5 on 2020-09-25 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_custom_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('user_f_name', models.CharField(max_length=100)),
                ('user_l_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('email_id', models.CharField(max_length=150, unique=True)),
                ('ph_no', models.IntegerField(unique=True)),
                ('passwd', models.CharField(max_length=254)),
                ('is_active', models.BooleanField(default=True)),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'user_account',
            },
        ),
        migrations.CreateModel(
            name='UserWishList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wish_list_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('is_active', models.BooleanField(default=1)),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_login.UserAccount')),
            ],
            options={
                'db_table': 'wish_list',
            },
        ),
        migrations.CreateModel(
            name='UserCartList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_list_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('is_active', models.BooleanField(default=1)),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_login.UserAccount')),
            ],
            options={
                'db_table': 'cart_list',
            },
        ),
    ]
