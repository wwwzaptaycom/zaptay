from django.db import models

from admin_login.models import zaptayAdmin
from django.utils import timezone
from django.utils.timezone import now
from datetime import datetime
import time

# Create your models here.

class Seller(models.Model):
    seller_id = models.CharField(max_length=100, blank=True, null=True)
    seller_title = models.CharField(max_length=100)
    seller_name = models.CharField(max_length=100)
    seller_email_id = models.CharField(max_length=200)
    seller_phone_no = models.CharField(max_length=20)
    seller_gst_no = models.CharField(max_length=200, blank=True, null=True)
    seller_aadhaar_no = models.CharField(max_length=20, blank=True, null=True)
    seller_voter_no = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=1)
    added_by = models.ForeignKey(zaptayAdmin, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(default=now)
    create_date = models.DateTimeField(default=now)

    class Meta:
        db_table = 'seller'

    def save(self, *args, **kwargs):
        if len(Seller.objects.all().order_by('-id')) == 0:
            get_max_id = 0
            mod_id = get_max_id+1
        else:
            get_max_id = Seller.objects.all().order_by('-id')[0]
            mod_id = get_max_id.id+1
        mod_id = str(mod_id).zfill(6)
        today = datetime.today()
        self.seller_id = 'SELLER-'+str(today.year)+'-'+str(int(time.time()))+'-'+str(mod_id)
        super(Seller, self).save(*args, **kwargs)

    def __str__(self):
        return self.seller_title
