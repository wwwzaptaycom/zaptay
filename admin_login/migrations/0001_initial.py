# Generated by Django 3.0.5 on 2020-07-22 11:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='zaptayAdmin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('admin_f_name', models.CharField(max_length=50)),
                ('admin_l_name', models.CharField(max_length=50)),
                ('admin_type', models.CharField(max_length=20)),
                ('emai_id', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=254)),
                ('account_status', models.IntegerField()),
                ('phone_no', models.BigIntegerField()),
                ('modify_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'zaptay_admin',
            },
        ),
    ]