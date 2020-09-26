# Generated by Django 3.0.5 on 2020-09-25 10:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('admin_login', '0002_auto_20200722_1147'),
        ('attribute', '0007_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnderTertiaryCategory',
            fields=[
                ('under_ter_category_id', models.AutoField(primary_key=True, serialize=False)),
                ('under_ter_category_name', models.CharField(max_length=255)),
                ('under_ter_category_seo_url', models.CharField(default='', max_length=255)),
                ('under_tertiary_category_image', models.ImageField(default='', upload_to='under_tertiary_category/images')),
                ('is_active', models.BooleanField(default=1)),
                ('modify_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_login.zaptayAdmin')),
                ('ter_category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attribute.TertiaryCategory')),
            ],
            options={
                'db_table': 'under_tertiary_category',
            },
        ),
    ]
