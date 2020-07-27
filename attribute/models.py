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
