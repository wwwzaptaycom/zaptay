from django.db import models

from django.utils import timezone
from django.utils.timezone import now
from datetime import datetime

# Create your models here.

class zaptayAdmin(models.Model):
    id = models.AutoField(primary_key=True)
    admin_f_name = models.CharField(max_length=50)
    admin_l_name = models.CharField(max_length=50)
    admin_type = models.CharField(max_length=20)
    email_id = models.CharField(max_length=100)
    password = models.CharField(max_length=254)
    account_status = models.IntegerField()
    phone_no = models.BigIntegerField()
    modify_date = models.DateTimeField(default=now)
    create_date = models.DateTimeField(default=now)

    class Meta:
        db_table = 'zaptay_admin'

    def __str__(self):
        return self.email_id
