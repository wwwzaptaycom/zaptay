# Generated by Django 3.0.5 on 2020-09-07 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20200823_1242'),
        ('user_login', '0003_userwishlist'),
    ]

    operations = [
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
