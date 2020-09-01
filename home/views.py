from django.shortcuts import render
from django.views.generic import View, TemplateView, FormView

from django.db.models import Subquery

from banner.models import Banner
from category.models import MainCategory
from attribute.models import SubCategory, TertiaryCategory
from product.models import Product, ProductImage
from stock.models import Bach

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
            exclusive_image['category_seo_name'] = exclusive.sub_category_name.replace(" ", "_")
            exclusive_image['category_name'] = exclusive.sub_category_name.replace("_", " ")
            exclusive_image['category_image'] = exclusive.sub_category_image
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

            weekly_dels_product_price = Bach.objects.filter(product_id=product).first()
            # print (weekly_dels_product_price)
            weekly_deals_dict['product_main_price'] = weekly_dels_product_price.main_price
            weekly_deals_dict['product_offer_price'] = weekly_dels_product_price.offer_price
            # ********************************************************************************************
            # Off Price Calculate
            # ********************************************************************************************
            if weekly_dels_product_price.offer_price:
                discount_percent = int(100-((float(weekly_dels_product_price.offer_price)/float(weekly_dels_product_price.main_price))*100))
                weekly_deals_dict['product_offer_percent'] = discount_percent
            else:
                weekly_deals_dict['product_offer_percent'] = 0
            # print (discount_percent)
            # **********************************************************************************************
            # **********************************************************************************************
            weekly_deals_list.append(weekly_deals_dict)
        # print (weekly_deals_list)

        # Featured category (men)
        '''
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
        '''

        manfashion_ter_category = TertiaryCategory.objects.filter(sub_category_id__in=Subquery(SubCategory.objects.filter(sub_category_name='men').values('sub_category_id')))
        menfashion_ter = list()
        for i in manfashion_ter_category:
            menfashion = dict()
            menfashion['ter_category_id'] = i.ter_category_id
            menfashion['ter_category_name'] = i.ter_category_name
            menfashion['ter_image'] = i.tertiary_category_image

            menfashion_ter.append(menfashion)
        # print (menfashion_ter)

        # Featured category (women)
        womanfashion_ter_category = TertiaryCategory.objects.filter(sub_category_id__in=Subquery(SubCategory.objects.filter(sub_category_name='women').values('sub_category_id')))
        womenfashion_ter = list()
        for i in womanfashion_ter_category:
            womenfashion = dict()
            womenfashion['ter_category_id'] = i.ter_category_id
            womenfashion['ter_category_name'] = i.ter_category_name
            womenfashion['ter_image'] = i.tertiary_category_image

            womenfashion_ter.append(womenfashion)

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

        # Men fashion Dreals
        men_fashion_dreals_list_db = Product.objects.filter(prod_sub_category__in=Subquery(
                                    SubCategory.objects.filter(sub_category_name='men').values('sub_category_id')
                                )).order_by('-id')
        # print (men_fashion_dreals_list_db)
        men_fashion_dreals_list = list()
        for men_fashion in men_fashion_dreals_list_db:
            men_fashion_dreals_dict = dict()
            men_fashion_dreals_dict['product_id'] = men_fashion.prod_custom_id
            men_fashion_dreals_dict['product_name'] = men_fashion.prod_title
            men_fashion_dreals_image_list_db = ProductImage.objects.filter(product_id=men_fashion, home_image=True).values('product_image', 'prod_image_title')
            if men_fashion_dreals_image_list_db:
                for image in men_fashion_dreals_image_list_db:
                    men_fashion_dreals_dict['product_image'] = image['product_image']
                    men_fashion_dreals_dict['product_image_title'] = image['prod_image_title']
            else:
                men_fashion_dreals_dict['product_image'] = ''
                men_fashion_dreals_dict['product_image_title'] = ''

            men_fashion_dreals_price_list_db = Bach.objects.filter(product_id=men_fashion)
            if men_fashion_dreals_price_list_db:
                for price in men_fashion_dreals_price_list_db:
                    men_fashion_dreals_dict['product_main_price'] = price.main_price
                    men_fashion_dreals_dict['product_offer_price'] = price.offer_price
                    men_fashion_dreals_dict['product_save_price'] = int(float(price.main_price)-float(price.offer_price))
                    men_fashion_dreals_dict['product_save_price_percent'] = int(100-((float(price.offer_price)/float(price.main_price))*100))
            else:
                men_fashion_dreals_dict['product_main_price'] = ''
                men_fashion_dreals_dict['product_offer_price'] = ''
                men_fashion_dreals_dict['product_save_price'] = ''
                men_fashion_dreals_dict['product_save_price_percent'] = ''
            men_fashion_dreals_list.append(men_fashion_dreals_dict)
        # print (men_fashion_dreals_list)

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
                    # 'men_fashion_product': menfashion,
                    'men_fashion': menfashion_ter,
                    # 'women_fashion_product': womenfashion,
                    'women_fashion': womenfashion_ter,
                    'electronic': electronic_list,
                    'man_fashion_dreals': men_fashion_dreals_list}
        return context
