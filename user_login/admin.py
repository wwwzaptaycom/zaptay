from django.contrib import admin
from . models  import UserAccount, UserWishList, UserCartList

# Register your models here.

admin.site.register(UserAccount)
admin.site.register(UserWishList)
admin.site.register(UserCartList)
