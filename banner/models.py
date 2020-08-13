from django.db import models
from admin_login.models import zaptayAdmin

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

    def __str__(self):
        return self.banner_name
