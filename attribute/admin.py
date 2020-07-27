from django.contrib import admin

from category.models import MainCategory
from attribute.models import SubCategory, TertiaryCategory

# Register your models here.

admin.site.register(MainCategory)
admin.site.register(SubCategory)
admin.site.register(TertiaryCategory)
