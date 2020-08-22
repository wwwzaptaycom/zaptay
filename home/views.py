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

        # Exclusive category
        exclusive_category = SubCategory.objects.filter(category_id__in=Subquery(MainCategory.objects.filter(main_category_name='exclusive').values('category_id')))
        exclusivefashion = list()
        for exclusive in exclusive_category:
            exclusive_image = dict()
            # print (exclusive.sub_category_name)
            exclusive_image['category_id'] = exclusive.sub_category_id
            exclusive_image['category_name'] = exclusive.sub_category_name.replace("_", " ")
            product = Product.objects.all().filter(prod_sub_category=exclusive.sub_category_id).order_by('-id')[:1]
            if product:
                for product_id in product:
                    product_image = ProductImage.objects.filter(product_id=product_id.id, home_image=True).values('product_image', 'prod_image_title')
                    if product_image:
                        exclusive_image['image'] = product_image[0]['product_image']
                        exclusive_image['image_title'] = product_image[0]['prod_image_title']
                    else:
                        exclusive_image['image'] = ""
                        exclusive_image['image_title'] = ""
            else:
                exclusive_image['image'] = ""
                exclusive_image['image_title'] = ""

            exclusivefashion.append(exclusive_image)

        #Weekly Deals & Offer
        weekly_dels_product = Product.objects.filter(weekly_dreals=True)
        weekly_deals_list = list()
        for product in weekly_dels_product:
            weekly_deals_dict = dict()
            weekly_deals_dict['product_id'] = product.prod_custom_id
            weekly_deals_dict['product_name'] = product.prod_title
            weekly_dels_product_image = ProductImage.objects.filter(product_id=product, home_image=True).values('prod_image_title', 'product_image')
            if weekly_dels_product_image:
                weekly_deals_dict['product_image'] = weekly_dels_product_image[0]['product_image']
                weekly_deals_dict['product_image_title'] = weekly_dels_product_image[0]['prod_image_title']
            else:
                weekly_deals_dict['product_image'] = ''
                weekly_deals_dict['product_image_title'] = ''
            weekly_deals_list.append(weekly_deals_dict)
        # print (weekly_deals_list)

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

        # Featured category (women)
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
            womenfashion.append(womenfashion_image)

        # Featured category (Electronic)
        electronic_product = Product.objects.filter(prod_sub_category__in=Subquery(SubCategory.objects.filter(sub_category_name='electronics').values('sub_category_id'))).order_by('-id')
        electronic_list = list()
        for electronic in electronic_product:
            electronic_dict = dict()
            electronic_dict['product_id'] = electronic.prod_custom_id
            electronic_dict['product_name'] = electronic.prod_title
            electronic_image = ProductImage.objects.filter(product_id=electronic, home_image=True).values('product_image', 'prod_image_title')
            if electronic_image:
                for img in electronic_image:
                    electronic_dict['product_image'] = img['product_image']
                    electronic_dict['product_image_title'] = img['prod_image_title']
            else:
                electronic_dict['product_image'] = ''
                electronic_dict['product_image_title'] = ''

            electronic_list.append(electronic_dict)

        context = {"page_name": "banner",
                    'mens_banner_image': get_mens_fashion,
                    'womens_banner_image': get_womens_fashion,
                    'baby_kid_banner_image': get_baby_kid_fashion,
                    'mobile_banner_image': get_mobile_fashion,
                    'electronic_banner_image': get_electronic_fashion,
                    'electronic_office_image': get_office_fashion,
                    'banner_1': banner_1,
                    'banner_2': banner_2,
                    'exclusive_category': exclusivefashion,
                    'weekly_dreals': weekly_deals_list,
                    'men_fashion_product': menfashion,
                    'women_fashion_product': womenfashion,
                    'electronic': electronic_list}
        return context
