# Generated by Django 3.0.5 on 2020-08-06 13:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin_login', '0002_auto_20200722_1147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_id', models.CharField(blank=True, max_length=100, null=True)),
                ('seller_title', models.CharField(max_length=100)),
                ('seller_email_id', models.CharField(max_length=200)),
                ('seller_phone_no', models.CharField(max_length=20)),
                ('seller_gst_no', models.CharField(blank=True, max_length=200, null=True)),
                ('seller_aadhaar_no', models.CharField(blank=True, max_length=20, null=True)),
                ('seller_voter_no', models.CharField(blank=True, max_length=100, null=True)),
                ('is_active', models.BooleanField(default=1)),
                ('modify_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_login.zaptayAdmin')),
            ],
            options={
                'db_table': 'seller',
            },
        ),
    ]