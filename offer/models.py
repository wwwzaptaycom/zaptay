from django.db import models

from admin_login.models import zaptayAdmin
from product.models import Product
from stock.models import Bach

from django.utils import timezone
from django.utils.timezone import now
from datetime import datetime
import time

# Create your models here.

class Offer(models.Model):
    offer_custom_id = models.CharField(max_length=150, unique=True, null=True, blank=True)
    offer_title = models.CharField(max_length=250)
    offer_start = models.DateTimeField()
    offer_end = models.DateTimeField()
    offer_status = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    added_by = models.ForeignKey(zaptayAdmin, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    '''
    modify_date.editable=True
    create_date.editable=True
    '''

    class Meta:
        db_table = "offers"

    def save(self, *args, **kwargs):
        if self.offer_custom_id == None:
            if len(Offer.objects.all().order_by('-id')) == 0:
                get_max_id = 0
                mod_id = get_max_id+1
            else:
                get_max_id = Offer.objects.all().order_by('-id')[0]
                mod_id = get_max_id.id+1
            mod_id = str(mod_id).zfill(6)
            today = datetime.today()
            self.offer_custom_id = 'offer-'+str(today.year)+'-'+str(int(time.time()))+'-'+str(mod_id)
        super(Offer, self).save(*args, **kwargs)

    def __str__(self):
        return self.offer_title

class OfferProduct(models.Model):
    offer_product_id = models.CharField(max_length=150, unique=True, null=True, blank=True)
    offer_id = models.ForeignKey(Offer, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    bach_id = models.ForeignKey(Bach, on_delete=models.CASCADE, blank=True, null=True)
    extra_offer_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    added_by = models.ForeignKey(zaptayAdmin, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    modify_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)
    '''
    modify_date.editable=True
    create_date.editable=True
    '''

    class Meta:
        db_table = "offer_products"

    def save(self, *args, **kwargs):
        if self.offer_product_id == None:
            if len(OfferProduct.objects.all().order_by('-id')) == 0:
                get_max_id = 0
                mod_id = get_max_id+1
            else:
                get_max_id = OfferProduct.objects.all().order_by('-id')[0]
                mod_id = get_max_id.id+1
            mod_id = str(mod_id).zfill(6)
            today = datetime.today()
            self.offer_product_id = 'offer-pro-'+str(today.year)+'-'+str(int(time.time()))+'-'+str(mod_id)
        super(OfferProduct, self).save(*args, **kwargs)

    def __str__(self):
        return self.offer_product_id
