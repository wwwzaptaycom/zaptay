from django.db import models
from product.models import Product

from admin_login.models import zaptayAdmin

from django.utils import timezone
from django.utils.timezone import now
from datetime import datetime
import time

# Create your models here.
class Bach(models.Model):
    bach_id = models.CharField(max_length=200, unique=True, blank=True, null=True)
    stock = models.IntegerField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    main_price = models.DecimalField(max_digits=10, decimal_places=2)
    offer_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=1)
    added_by = models.ForeignKey(zaptayAdmin, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)
    '''
    modify_date.editable=True
    create_date.editable=True
    '''

    class Meta:
        db_table = "bach"

    def save(self, *args, **kwargs):
        if self.bach_id == None:
            if len(Bach.objects.all().order_by('-id')) == 0:
                get_max_id = 0
                mod_id = get_max_id+1
            else:
                get_max_id = Bach.objects.all().order_by('-id')[0]
                mod_id = get_max_id.id+1
            mod_id = str(mod_id).zfill(6)
            today = datetime.today()
            self.bach_id = 'bach-'+str(today.year)+'-'+str(int(time.time()))+'-'+str(mod_id)
        super(Bach, self).save(*args, **kwargs)

    def __str__(self):
        return self.bach_id
