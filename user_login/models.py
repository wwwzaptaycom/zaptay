from django.db import models

from django.utils import timezone
from django.utils.timezone import now
from datetime import datetime
import time

from product.models import Product

# Create your models here.

class UserAccount(models.Model):
    user_custom_id = models.CharField(max_length=100, unique=True, blank=True, null=True)
    user_f_name = models.CharField(max_length=100)
    user_l_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    email_id = models.CharField(max_length=150, unique=True)
    ph_no = models.IntegerField(unique=True)
    passwd = models.CharField(max_length=254)
    is_active = models.BooleanField(default=True)
    modify_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)
    '''
    modify_date.editable=True
    create_date.editable=True
    '''

    class Meta:
        db_table = "user_account"

    def save(self, *args, **kwargs):
        # print ("******************************")
        # print (self.user_custom_id)
        if self.user_custom_id == None:
            if len(UserAccount.objects.all().order_by('-id')) == 0:
                get_max_id = 0
                mod_id = get_max_id+1
            else:
                get_max_id = UserAccount.objects.all().order_by('-id')[0]
                mod_id = get_max_id.id+1
            mod_id = str(mod_id).zfill(6)
            today = datetime.today()
            self.user_custom_id = 'user-'+str(today.year)+'-'+str(int(time.time()))+'-'+str(mod_id)
        super(UserAccount, self).save(*args, **kwargs)

    def __str__(self):
        return self.user_custom_id

class UserWishList(models.Model):
    wish_list_id = models.CharField(max_length=100, unique=True, blank=True, null=True)
    user_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE, blank=False)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False)
    is_active = models.BooleanField(default=1)
    modify_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "wish_list"

    def save(self, *args, **kwargs):
        # print ("******************************")
        # print (self.user_custom_id)
        if self.wish_list_id == None:
            if len(UserWishList.objects.all().order_by('-id')) == 0:
                get_max_id = 0
                mod_id = get_max_id+1
            else:
                get_max_id = UserWishList.objects.all().order_by('-id')[0]
                mod_id = get_max_id.id+1
            mod_id = str(mod_id).zfill(6)
            today = datetime.today()
            self.wish_list_id = 'wish-list-'+str(today.year)+'-'+str(int(time.time()))+'-'+str(mod_id)
        super(UserWishList, self).save(*args, **kwargs)

    def __str__(self):
        return self.wish_list_id


class UserCartList(models.Model):
    cart_list_id = models.CharField(max_length=100, unique=True, blank=True, null=True)
    user_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE, blank=False)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False)
    is_active = models.BooleanField(default=1)
    modify_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "cart_list"

    def save(self, *args, **kwargs):
        # print ("******************************")
        # print (self.user_custom_id)
        if self.cart_list_id == None:
            if len(UserCartList.objects.all().order_by('-id')) == 0:
                get_max_id = 0
                mod_id = get_max_id+1
            else:
                get_max_id = UserCartList.objects.all().order_by('-id')[0]
                mod_id = get_max_id.id+1
            mod_id = str(mod_id).zfill(6)
            today = datetime.today()
            self.cart_list_id = 'cart-'+str(today.year)+'-'+str(int(time.time()))+'-'+str(mod_id)
        super(UserCartList, self).save(*args, **kwargs)

    def __str__(self):
        return self.cart_list_id
