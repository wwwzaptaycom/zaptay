from django.db import models
from admin_login.models import zaptayAdmin

from datetime import datetime
import time

# Create your models here.

class Banner(models.Model):
    banner_id = models.CharField(max_length=100, blank=True, null=True)
    banner_image = models.ImageField(upload_to="banner/men_fashion/images", default="", blank=True, null=True)
    banner_name = models.CharField(max_length=50, blank=True, null=True)
    banner_link = models.URLField(max_length = 200, blank=True, null=True)
    added_by = models.ForeignKey(zaptayAdmin, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(auto_now=True)
    added_date = models.DateTimeField(auto_now_add=True)
    # added_date.editable=True

    class Meta:
        db_table = "banners"

    def save(self, *args, **kwargs):
        if self.banner_id == None:
            if len(Banner.objects.all().order_by('-id')) == 0:
                get_max_id = 0
                mod_id = get_max_id+1
            else:
                get_max_id = Banner.objects.all().order_by('-id')[0]
                mod_id = get_max_id.id+1
            mod_id = str(mod_id).zfill(6)
            today = datetime.today()
            self.banner_id = 'BAN-'+str(today.year)+'-'+str(int(time.time()))+'-'+str(mod_id)
        super(Banner, self).save(*args, **kwargs)

    def __str__(self):
        return self.banner_name
