from django.shortcuts import render
from django.views.generic import View, TemplateView, FormView

from django.db.models import Subquery

from banner.models import Banner
from category.models import MainCategory
from attribute.models import SubCategory, TertiaryCategory
from product.models import Product, ProductImage
from stock.models import Bach, Inventory
from offer.models import Offer, OfferProduct
from user_login.models import UserAccount

from django.utils import timezone
from datetime import datetime

from home.base_template import BaseTemplateHeader

# Create your views here.

class CartListView(TemplateView):
    template_name = 'user_template/cartlist.html'

    def get_context_data(self, **kwargs):
        context = dict()

        header_logo = get_header_logo = Banner.objects.filter(banner_name='header_logo').order_by('-id').first()

        megamenu = list()
        featured_category = MainCategory.objects.filter(main_category_name='featured').first()
        get_sub_category = SubCategory.objects.filter(category_id=featured_category)
        for i in get_sub_category:
            sub_category = list()
            sub_category.append(i.sub_category_name)
            get_tertiary_category = TertiaryCategory.objects.filter(sub_category_id=i)
            tertiary_cate_ar = list()
            for j in get_tertiary_category:
                tertiary_cate = dict()
                tertiary_cate['id'] = j.ter_category_id
                tertiary_cate['name'] = j.ter_category_name
                tertiary_cate_ar.append(tertiary_cate)
            sub_category.append(tertiary_cate_ar)
            megamenu.append(sub_category)
        # print (megamenu)

        featured_category = MainCategory.objects.filter(main_category_name='exclusive').first()
        get_more_sub_category = SubCategory.objects.filter(category_id=featured_category)
        # print (featured_category)

        obj = BaseTemplateHeader(self.request)
        base_template_data = obj.GetHeaderContent()

        context = {
            'base_template_content': base_template_data,
            # 'header_logo': header_logo,
            # 'mega_menu_sub_category': megamenu,
            # 'mega_menu_more_category': get_more_sub_category,
        }

        return context
