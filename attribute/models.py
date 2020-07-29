from django.db import models

from django.utils import timezone
from django.utils.timezone import now
from datetime import datetime

from admin_login.models import zaptayAdmin
from category.models import MainCategory

# Create your models here.

class SubCategory(models.Model):
    sub_category_id = models.AutoField(primary_key=True)
    sub_category_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=1)
    added_by = models.ForeignKey(zaptayAdmin, on_delete=models.CASCADE)
    category_id = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(default=now)
    create_date = models.DateTimeField(default=now)

    class Meta:
        db_table = "sub_category"

    def __str__(self):
        return self.sub_category_name

class TertiaryCategory(models.Model):
    ter_category_id = models.AutoField(primary_key=True)
    ter_category_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=1)
    added_by = models.ForeignKey(zaptayAdmin, on_delete=models.CASCADE)
    sub_category_id = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(default=now)
    create_date = models.DateTimeField(default=now)

    class Meta:
        db_table = "tertiary_category"

    def __str__(self):
        return self.ter_category_name

class Colour(models.Model):
    color_id = models.AutoField(primary_key=True)
    color_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=1)
    added_by = models.ForeignKey(zaptayAdmin, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(default=now)
    create_date = models.DateTimeField(default=now)

    class Meta:
        db_table = "colours"

    def __str__(self):
        return self.color_name

class Size(models.Model):
    size_id = models.AutoField(primary_key=True)
    size_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=1)
    added_by = models.ForeignKey(zaptayAdmin, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(default=now)
    create_date = models.DateTimeField(default=now)

    class Meta:
        db_table = "size"

    def __str__(self):
        return self.size_name

class Source(models.Model):
    source_id = models.AutoField(primary_key=True)
    source_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=1)
    added_by = models.ForeignKey(zaptayAdmin, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(default=now)
    create_date = models.DateTimeField(default=now)

    class Meta:
        db_table = "source"

    def __str__(self):
        return self.source_name
