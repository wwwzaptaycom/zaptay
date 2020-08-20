from django.shortcuts import render
from django.views.generic import View, TemplateView, FormView

from django.db.models import Subquery

from banner.models import Banner
from category.models import MainCategory
from attribute.models import SubCategory, TertiaryCategory
from product.models import Product, ProductImage

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = dict()
        get_mens_fashion = Banner.objects.filter(banner_name='men_banner').values('id', 'banner_image', 'banner_link')
        # print (get_mens_fashion)
        get_womens_fashion = Banner.objects.filter(banner_name='women_banner').values('id', 'banner_image', 'banner_link')
        get_baby_kid_fashion = Banner.objects.filter(banner_name='baby_kid_banner').values('id', 'banner_image', 'banner_link')
        get_mobile_fashion = Banner.objects.filter(banner_name='mobile_banner').values('id', 'banner_image', 'banner_link')
        get_electronic_fashion = Banner.objects.filter(banner_name='electronic_banner').values('id', 'banner_image', 'banner_link')
        get_office_fashion = Banner.objects.filter(banner_name='office_appliance_banner').values('id', 'banner_image', 'banner_link')

        banner_1 = Banner.objects.filter(banner_name='advatice_1').order_by('-id')[0:3]
        banner_2 = Banner.objects.filter(banner_name='advatice_2').order_by('-id')[0:2]

        # ********************************************************************************************************
        # *************************************    Product fetching    *******************************************
        # ********************************************************************************************************

        # Featured category (men)
        menfashion_product = Product.objects.filter(prod_sub_category__in=Subquery(SubCategory.objects.filter(sub_category_name='men').values('sub_category_id')))
        menfashion = list()
        for i in menfashion_product:
            menfashion_image = dict()
            menfashion_image['product_id'] = i.prod_custom_id
            menfashion_image['product_name'] = i.prod_title
            product_image = ProductImage.objects.filter(product_id=i, home_image=True).values('product_image', 'prod_image_title')
            if product_image:
                for img in product_image:
                    menfashion_image['product_image'] = img['product_image']
                    menfashion_image['product_image_title'] = img['prod_image_title']
            else:
                menfashion_image['product_image'] = ''
                menfashion_image['product_image_title'] = ''

            # menfashion_image.append(ProductImage.objects.filter(product_id=i, home_image=True).values('product_image', 'prod_image_title'))
            menfashion.append(menfashion_image)

        womenfashion_product = Product.objects.filter(prod_sub_category__in=Subquery(SubCategory.objects.filter(sub_category_name='women').values('sub_category_id')))
        womenfashion = list()
        for i in womenfashion_product:
            womenfashion_image = dict()
            womenfashion_image['product_id'] = i.prod_custom_id
            womenfashion_image['product_name'] = i.prod_title
            product_image = ProductImage.objects.filter(product_id=i, home_image=True).values('product_image', 'prod_image_title')
            if product_image:
                for img in product_image:
                    womenfashion_image['product_image'] = img['product_image']
                    womenfashion_image['product_image_title'] = img['prod_image_title']
            else:
                womenfashion_image['product_image'] = ''
                womenfashion_image['product_image_title'] = ''

            # womenfashion_image.append(ProductImage.objects.filter(product_id=i, home_image=True).values('product_image', 'prod_image_title'))
            womenfashion.append(womenfashion_image)

        context = {"page_name": "banner",
                    'mens_banner_image': get_mens_fashion,
                    'womens_banner_image': get_womens_fashion,
                    'baby_kid_banner_image': get_baby_kid_fashion,
                    'mobile_banner_image': get_mobile_fashion,
                    'electronic_banner_image': get_electronic_fashion,
                    'electronic_office_image': get_office_fashion,
                    'banner_1': banner_1,
                    'banner_2': banner_2,
                    'men_fashion_product': menfashion,
                    'women_fashion_product': womenfashion}
        return context
