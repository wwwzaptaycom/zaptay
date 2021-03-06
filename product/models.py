from django.db import models
from category.models import MainCategory
from attribute.models import SubCategory, TertiaryCategory, UnderTertiaryCategory, Brand, Colour, Size, Source, SameDayDelivary, NextDayDelivary
from seller.models import Seller
from admin_login.models import zaptayAdmin

from django.utils import timezone
from django.utils.timezone import now
from datetime import datetime
import time

# Create your models here.
'''
class Product(models.Model):
    prod_custom_id = models.CharField(max_length=200, blank=False)
    prod_title = models.CharField(max_length=250)
    prod_main_price = models.DecimalField(max_digits=10, decimal_places=2)
    prod_offer_price = models.DecimalField(max_digits=10, decimal_places=2)
    prod_extra_price = models.DecimalField(max_digits=10, decimal_places=2)
    prod_purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    prod_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE, blank=False)
    prod_sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=False)
    prod_tertiary_category = models.ForeignKey(TertiaryCategory, on_delete=models.CASCADE, blank=False)
    prod_color = models.ForeignKey(Colour, on_delete=models.CASCADE, blank=False)
    prod_size = models.ForeignKey(Size, on_delete=models.CASCADE, blank=False)
    prod_made_in = models.ForeignKey(Source, on_delete=models.CASCADE, blank=False)
    prod_desc = models.CharField(max_length=300,blank=False)
    same_day_delivery = models.BooleanField(default=False)
    same_day_delivery_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    next_day_delivery = models.BooleanField(default=False)
    next_day_delivery_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    customize_day_delivery = models.BooleanField(default=False)
    customize_day_delivery_day = models.IntegerField(blank = True)
    customize_day_delivery_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    weekly_dreals = models.BooleanField(default=False)
    top_offer = models.BooleanField(default=False)
    product_return = models.BooleanField(default=False)
    cash_on_delivery = models.BooleanField(default=False)
    youtube_link = models.URLField(max_length=300, blank=True)
    is_active = models.BooleanField(default=1)
    added_by = models.ForeignKey(zaptayAdmin, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(default=now)
    create_date = models.DateTimeField(default=now)


    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.prod_title
'''

class Product(models.Model):
    prod_custom_id = models.CharField(max_length=200, unique=True, blank=True, null=True)
    prod_title = models.CharField(max_length=250)

    prod_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE, blank=False, null=False)
    prod_sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=False)
    prod_tertiary_category = models.ForeignKey(TertiaryCategory, on_delete=models.CASCADE, blank=True, null=True)
    prod_under_tertiary_category = models.ForeignKey(UnderTertiaryCategory, on_delete=models.CASCADE, blank=True, null=True)
    prod_brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=False, null=False)
    prod_color = models.ForeignKey(Colour, on_delete=models.CASCADE, blank=False)
    prod_size = models.ForeignKey(Size, on_delete=models.CASCADE, blank=False)
    prod_made_in = models.ForeignKey(Source, on_delete=models.CASCADE, blank=False)
    prod_desc = models.TextField(blank=False)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    same_day_delivery = models.BooleanField(default=False)
    same_day_delivery_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    next_day_delivery = models.BooleanField(default=False)
    next_day_delivery_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    customize_day_delivery = models.BooleanField(default=False)
    customize_day_delivery_day = models.IntegerField(blank = True)
    customize_day_delivery_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    weekly_dreals = models.BooleanField(default=False)
    top_offer = models.BooleanField(default=False)
    product_return = models.BooleanField(default=False)
    cash_on_delivery = models.BooleanField(default=False)
    youtube_link = models.URLField(max_length=300, blank=True)
    is_active = models.BooleanField(default=1)
    added_by = models.ForeignKey(zaptayAdmin, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(default=now)
    create_date = models.DateTimeField(default=now)


    class Meta:
        db_table = 'products'

    def save(self, *args, **kwargs):
        if self.prod_custom_id == None:
            if len(Product.objects.all().order_by('-id')) == 0:
                get_max_id = 0
                mod_id = get_max_id+1
            else:
                get_max_id = Product.objects.all().order_by('-id')[0]
                mod_id = get_max_id.id+1
            mod_id = str(mod_id).zfill(6)
            today = datetime.today()
            self.prod_custom_id = 'PROD-'+str(today.year)+'-'+str(int(time.time()))+'-'+str(mod_id)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.prod_title

class ProductImage(models.Model):
    prod_image_id = models.CharField(max_length=200, unique=True, blank=True, null=True)
    prod_image_title = models.CharField(max_length=200)
    product_image = models.ImageField(upload_to="products/images", default="")
    product_img_sl_no = models.IntegerField(blank = True, null=True, default=0)
    home_image = models.BooleanField(default=False)
    added_by = models.ForeignKey(zaptayAdmin, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(default=now)
    create_date = models.DateTimeField(default=now)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = "product_images"

    def save(self, *args, **kwargs):
        if self.prod_image_id == None:
            print (len(ProductImage.objects.all().order_by('-id')))
            if len(ProductImage.objects.all().order_by('-id')) == 0:
                get_max_id = 0
                mod_id = get_max_id+1
            else:
                get_max_id = ProductImage.objects.all().order_by('-id')[0]
                mod_id = get_max_id.id+1
            mod_id = str(mod_id).zfill(6)
            today = datetime.today()
            self.prod_image_id = 'PROD-IMG-'+str(today.year)+'-'+str(int(time.time()))+'-'+str(mod_id)
        super(ProductImage, self).save(*args, **kwargs)

    def __str__(self):
        return "Image - "+self.prod_image_title
