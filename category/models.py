from django.db import models
from django.utils import timezone
from django.utils.timezone import now
from datetime import datetime

# Admin part
from admin_login.models import zaptayAdmin

# Create your models here.

class MainCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    main_category_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=1)
    added_by = models.ForeignKey(zaptayAdmin, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(default=now)
    create_date = models.DateTimeField(default=now)

    class Meta:
        db_table = "main_category"

    def __str__(self):
        return self.main_category_name
