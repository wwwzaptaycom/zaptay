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

from . base_template import BaseTemplateHeader

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
        banner_3 = Banner.objects.filter(banner_name='advatice_3').order_by('-id')[0:1]
        banner_4 = Banner.objects.filter(banner_name='advatice_4').order_by('-id')[0:2]
        banner_5 = Banner.objects.filter(banner_name='advatice_5').order_by('-id')[0:2]
        banner_6 = Banner.objects.filter(banner_name='advatice_6').order_by('-id')[0:1]

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

        # Offer (weekly begininh of the home page)
        offer_dic = dict()
        get_all_offer = Offer.objects.filter(offer_start__lte=timezone.now(), offer_end__gte=timezone.now(), is_active=True).first()
        # print (timezone.now())
        offer_products = list()
        if get_all_offer:
            offer_end_time = get_all_offer.offer_end.strftime("%b %d, %Y %H:%M:%S")
            offer_dic['title'] = get_all_offer.offer_title
            offer_dic['time_left'] = offer_end_time
            # print (get_all_offer.offer_custom_id, offer_end_time)

            get_offer_product = OfferProduct.objects.filter(offer_id=get_all_offer)
            # print (get_offer_product)
            # offer_products = list()
            if get_offer_product:
                for offer_prod in get_offer_product:
                    offer_product_dic = dict()
                    offer_product_dic['product_title'] = offer_prod.product_id.prod_title
                    offer_product_dic['product_custom_id'] = offer_prod.product_id.prod_custom_id
                    offer_product_dic['product_extra_offer_price'] = offer_prod.extra_offer_price

                    offer_product_image = ProductImage.objects.filter(product_id=offer_prod.product_id, home_image=True).first()
                    if offer_product_image:
                        offer_product_dic['product_image'] = offer_product_image.product_image
                        offer_product_dic['product_image_title'] = offer_product_image.prod_image_title

                    stock_price = Bach.objects.filter(product_id=offer_prod.product_id).first()
                    if stock_price:
                        offer_product_dic['product_main_price'] = stock_price.main_price
                        offer_product_dic['product_offer_price'] = stock_price.offer_price
                        offer_product_dic['product_save_price_percent'] = int(100-((float(offer_prod.extra_offer_price)/float(stock_price.main_price))*100))

                    offer_products.append(offer_product_dic)
        # print (offer_products)

            # import datetime as dt
            # a = dt.datetime(2017,9,4,11,34,00)
            # b = dt.datetime(2017,9,5,11,34,00)
            # print ((b-a).total_seconds()

        # Check user login
        user_detail = list()
        if self.request.COOKIES.get('user_id'):
            user_details_dict = dict()
            get_user_detail = UserAccount.objects.filter(user_custom_id=self.request.COOKIES.get('user_id'))
            user_details_dict = dict()
            user_details_dict['name'] = get_user_detail[0].user_f_name.capitalize()+" "+get_user_detail[0].user_l_name.capitalize()
            user_detail.append(user_details_dict)
            # print (user_detail)

        # Women Fashion Deals
        get_women_deals = list()
        get_women_fashion_items = Product.objects.filter(prod_sub_category__in=Subquery(SubCategory.objects.filter(sub_category_name__contains='women').values('sub_category_id'))).order_by('-id')
        # print (get_women_fashion_items)
        for women_fashion in get_women_fashion_items:
            get_women_deals_dic = dict()
            get_women_deals_dic['product_name'] = women_fashion.prod_title
            get_women_deals_dic['prod_custom_id'] = women_fashion.prod_custom_id
            women_fashio_image_db = ProductImage.objects.filter(product_id=women_fashion, home_image=True)
            # print (women_fashio_image_db)
            get_women_deals_dic['prod_image'] = women_fashio_image_db[0].product_image
            get_women_deals_dic['prod_image_title'] = women_fashio_image_db[0].prod_image_title

            women_bach_data_db = Bach.objects.filter(id__in=Subquery(Inventory.objects.filter(product_id=women_fashion, remaining_stock__gt=0, is_active=True).values('bach_id_id'))).first()
            # print (women_bach_data_db)
            get_women_deals_dic['main_price'] = women_bach_data_db.main_price
            get_women_deals_dic['offer_price'] = women_bach_data_db.offer_price

            get_women_deals_dic['product_save_price'] = int(float(women_bach_data_db.main_price)-float(women_bach_data_db.offer_price))
            get_women_deals_dic['product_save_price_percent'] = int(100-((float(women_bach_data_db.offer_price)/float(women_bach_data_db.main_price))*100))

            get_women_deals.append(get_women_deals_dic)

        # Mobile & Robotics Deals
        get_mobile_robotics = list()
        get_mobile_robotics_items = Product.objects.filter(prod_sub_category__in=Subquery(SubCategory.objects.filter(sub_category_name__contains='women').values('sub_category_id'))).order_by('-id')
        # print (get_women_fashion_items)
        for mobile_robotics in get_mobile_robotics_items:
            get_mobile_robotics_dic = dict()
            get_mobile_robotics_dic['product_name'] = mobile_robotics.prod_title
            get_mobile_robotics_dic['prod_custom_id'] = mobile_robotics.prod_custom_id
            mobile_robotics_image_db = ProductImage.objects.filter(product_id=mobile_robotics, home_image=True)
            # print (women_fashio_image_db)
            get_mobile_robotics_dic['prod_image'] = mobile_robotics_image_db[0].product_image
            get_mobile_robotics_dic['prod_image_title'] = mobile_robotics_image_db[0].prod_image_title

            mobile_robotics_bach_data_db = Bach.objects.filter(id__in=Subquery(Inventory.objects.filter(product_id=mobile_robotics, remaining_stock__gt=0, is_active=True).values('bach_id_id'))).first()
            # print (women_bach_data_db)
            get_mobile_robotics_dic['main_price'] = mobile_robotics_bach_data_db.main_price
            get_mobile_robotics_dic['offer_price'] = mobile_robotics_bach_data_db.offer_price

            get_mobile_robotics_dic['product_save_price'] = int(float(mobile_robotics_bach_data_db.main_price)-float(mobile_robotics_bach_data_db.offer_price))
            get_mobile_robotics_dic['product_save_price_percent'] = int(100-((float(mobile_robotics_bach_data_db.offer_price)/float(mobile_robotics_bach_data_db.main_price))*100))

            get_mobile_robotics.append(get_mobile_robotics_dic)

        # Shooses And Watchs
        get_shooses_watch = list()
        get_shooses_watch_items = Product.objects.filter(prod_sub_category__in=Subquery(SubCategory.objects.filter(sub_category_name__contains='women').values('sub_category_id'))).order_by('-id')
        # print (get_women_fashion_items)
        for shooses_watch in get_shooses_watch_items:
            get_shooses_watch_dic = dict()
            get_shooses_watch_dic['product_name'] = shooses_watch.prod_title
            get_shooses_watch_dic['prod_custom_id'] = shooses_watch.prod_custom_id
            shooses_watch_image_db = ProductImage.objects.filter(product_id=shooses_watch, home_image=True)
            # print (women_fashio_image_db)
            get_shooses_watch_dic['prod_image'] = shooses_watch_image_db[0].product_image
            get_shooses_watch_dic['prod_image_title'] = shooses_watch_image_db[0].prod_image_title

            shooses_watch_bach_data_db = Bach.objects.filter(id__in=Subquery(Inventory.objects.filter(product_id=shooses_watch, remaining_stock__gt=0, is_active=True).values('bach_id_id'))).first()
            # print (women_bach_data_db)
            get_shooses_watch_dic['main_price'] = shooses_watch_bach_data_db.main_price
            get_shooses_watch_dic['offer_price'] = shooses_watch_bach_data_db.offer_price

            get_shooses_watch_dic['product_save_price'] = int(float(shooses_watch_bach_data_db.main_price)-float(shooses_watch_bach_data_db.offer_price))
            get_shooses_watch_dic['product_save_price_percent'] = int(100-((float(shooses_watch_bach_data_db.offer_price)/float(shooses_watch_bach_data_db.main_price))*100))

            get_shooses_watch.append(get_shooses_watch_dic)

        # Top offer
        get_top_offer = list()
        get_top_offer_product = Product.objects.filter(top_offer=True)
        # print (get_top_offer_product)
        for offer_product in get_top_offer_product:
            get_top_offer_dic = dict()
            get_top_offer_dic['product_name'] = offer_product.prod_title
            get_top_offer_dic['prod_custom_id'] = offer_product.prod_custom_id
            get_top_offer_image_db = ProductImage.objects.filter(product_id=offer_product, home_image=True)
            # print (get_top_offer_image_db)
            get_top_offer_dic['product_image'] = get_top_offer_image_db[0].product_image
            get_top_offer_dic['prod_image_title'] = get_top_offer_image_db[0].prod_image_title

            top_offer_bach_data_db = Bach.objects.filter(id__in=Subquery(Inventory.objects.filter(product_id=offer_product, remaining_stock__gt=0, is_active=True).values('bach_id_id'))).first()
            # print (shooses_watch_bach_data_db)
            get_top_offer_dic['main_price'] = top_offer_bach_data_db.main_price
            get_top_offer_dic['offer_price'] = top_offer_bach_data_db.offer_price
            get_top_offer_dic['product_save_price'] = int(float(top_offer_bach_data_db.main_price)-float(top_offer_bach_data_db.offer_price))
            get_top_offer_dic['product_save_price_percent'] = int(100-((float(top_offer_bach_data_db.offer_price)/float(top_offer_bach_data_db.main_price))*100))

            get_top_offer.append(get_top_offer_dic)

        context = {"page_name": "banner",
                    'mens_banner_image': get_mens_fashion,
                    'womens_banner_image': get_womens_fashion,
                    'baby_kid_banner_image': get_baby_kid_fashion,
                    'mobile_banner_image': get_mobile_fashion,
                    'electronic_banner_image': get_electronic_fashion,
                    'electronic_office_image': get_office_fashion,
                    'banner_1': banner_1,
                    'banner_2': banner_2,
                    'banner_3': banner_3,
                    'banner_4': banner_4,
                    'banner_5': banner_5,
                    'banner_6': banner_6,
                    'exclusive_category': exclusivefashion,
                    'weekly_dreals': weekly_deals_list,
                    # 'men_fashion_product': menfashion,
                    'men_fashion': menfashion_ter,
                    # 'women_fashion_product': womenfashion,
                    'women_fashion': womenfashion_ter,
                    'electronic': electronic_list,
                    'man_fashion_dreals': men_fashion_dreals_list,
                    'deals': offer_dic,
                    'deals_product': offer_products,
                    'get_women_deals_list': get_women_deals,
                    'get_mobile_robotics_list': get_mobile_robotics,
                    'get_shooses_watch_list': get_shooses_watch,
                    'get_top_offer_list': get_top_offer,
                    'login_user': user_detail}
        return context

class Home2(TemplateView):
    template_name = "user_template/home.html"

    def get_context_data(self, **kwargs):
        context = dict()

        get_mens_fashion = Banner.objects.filter(banner_name='men_banner').values('id', 'banner_image', 'banner_link', 'banner_name_custom')
        # print (get_mens_fashion)
        get_womens_fashion = Banner.objects.filter(banner_name='women_banner').values('id', 'banner_image', 'banner_link', 'banner_name_custom')
        get_baby_kid_fashion = Banner.objects.filter(banner_name='baby_kid_banner').values('id', 'banner_image', 'banner_link', 'banner_name_custom')
        get_mobile_fashion = Banner.objects.filter(banner_name='mobile_banner').values('id', 'banner_image', 'banner_link', 'banner_name_custom')
        get_electronic_fashion = Banner.objects.filter(banner_name='electronic_banner').values('id', 'banner_image', 'banner_link', 'banner_name_custom')
        get_office_fashion = Banner.objects.filter(banner_name='office_appliance_banner').values('id', 'banner_image', 'banner_link', 'banner_name_custom')

        banner_1 = Banner.objects.filter(banner_name='advatice_1').order_by('-id')[0:3]
        banner_2 = Banner.objects.filter(banner_name='advatice_2').order_by('-id')[0:2]
        banner_3 = Banner.objects.filter(banner_name='advatice_3').order_by('-id')[0:1]
        banner_4 = Banner.objects.filter(banner_name='advatice_4').order_by('-id')[0:2]
        banner_5 = Banner.objects.filter(banner_name='advatice_5').order_by('-id')[0:2]
        banner_6 = Banner.objects.filter(banner_name='advatice_6').order_by('-id')[0:1]

        banner_right = Banner.objects.filter(banner_name='advatice_right').order_by('-id')[0:1]
        # banner_6 = Banner.objects.filter(banner_name='advatice_left').order_by('-id')[0:1]

        exclusive_category_id = MainCategory.objects.filter(main_category_name='exclusive').first()
        exclusive_category = SubCategory.objects.filter(category_id=exclusive_category_id)
        # print (exclusive_category)

        # ***************************************************************************************************************
        # *****************************  Weekly offer content start  ****************************************************
        # ***************************************************************************************************************
        get_today_offer = Offer.objects.filter(offer_start__lte=timezone.now(), offer_end__gte=timezone.now(), is_active=True).first()
        offer_products = list()
        if get_today_offer:
            start_time = get_today_offer.offer_start
            end_time = get_today_offer.offer_end
            # print (get_today_offer, start_time, end_time)
            get_today_offer_product_list = OfferProduct.objects.filter(offer_id=get_today_offer)
            # print (get_today_offer_product_list[0].product_id)

            for offer_product in get_today_offer_product_list:
                offer_products_dict = dict()
                # print (offer_product.product_id)
                get_stock = Inventory.objects.filter(product_id=offer_product.product_id, remaining_stock__gt = 0).first()
                if get_stock:
                    bach_id = get_stock.bach_id
                else:
                    get_bach = Bach.objects.filter(product_id=offer_product.product_id).order_by('-id').first()
                    bach_id = get_bach

                get_price = Bach.objects.filter(bach_id=bach_id).first()
                main_price = get_price.main_price
                offer_price = offer_product.extra_offer_price
                # print (get_price)

                product_name = offer_product.product_id.prod_title
                # print (product_name,main_price,offer_price)

                product_img = ProductImage.objects.filter(product_id=offer_product.product_id, home_image=True).first()
                # print (product_img)
                offer_products_dict['product_name'] = product_name
                offer_products_dict['product_image'] = product_img.product_image
                offer_products_dict['product_image_title'] = product_img.prod_image_title
                offer_products_dict['product_main_price'] = main_price
                offer_products_dict['product_offer_price'] = offer_price

                total_discount = int(100-((float(offer_price)/float(main_price)))*100)
                offer_products_dict['product_duscount'] = total_discount

                offer_products.append(offer_products_dict)
            # print(offer_products)

            # get_product_stock

            # from datetime import datetime, timedelta
            # time_threshold = datetime.now() - timedelta(hours=5)
            # print (time_threshold)

        # *****************************  Weekly offer content start  ****************************************************

        # ***************************************************************************************************************
        # *****************************  Featured Category content start  ****************************************************
        # ***************************************************************************************************************
        get_category = MainCategory.objects.filter(main_category_name='featured').first()
        get_sub_category = SubCategory.objects.filter(category_id=get_category)
        featured_category = list()
        for sub_category in get_sub_category:
            featured_category_dict = dict()
            get_tertitory_category = TertiaryCategory.objects.filter(sub_category_id=sub_category)
            featured_category_dict['sub_category'] = sub_category.sub_category_name
            featured_tertiary_category = list()
            for tertiary_category in  get_tertitory_category:
                featured_tertiary_category_dict = dict()
                featured_tertiary_category_dict['category_name'] = tertiary_category.ter_category_name
                featured_tertiary_category_dict['category_url'] = tertiary_category.ter_category_seo_url
                featured_tertiary_category_dict['category_image'] = tertiary_category.tertiary_category_image
                featured_tertiary_category.append(featured_tertiary_category_dict)
            featured_category_dict['tertiary_category'] = featured_tertiary_category
            featured_category.append(featured_category_dict)
        # print (featured_category)
        # *****************************  Featured Category content start  ****************************************************



        # ***************************************************************************************************************
        # *****************************  Electronnic Category content start  ****************************************************
        # ***************************************************************************************************************

        get_sub_category = SubCategory.objects.filter(sub_category_name='electronics').first()
        # print (get_sub_category)
        # featured_category = list()
        # for sub_category in get_sub_category:
        #     featured_category_dict = dict()
        #     get_tertitory_category = TertiaryCategory.objects.filter(sub_category_id=sub_category)
        #     featured_category_dict['sub_category'] = sub_category.sub_category_name
        #     featured_tertiary_category = list()
        #     for tertiary_category in  get_tertitory_category:
        #         featured_tertiary_category_dict = dict()
        #         featured_tertiary_category_dict['category_name'] = tertiary_category.ter_category_name
        #         featured_tertiary_category_dict['category_url'] = tertiary_category.ter_category_seo_url
        #         featured_tertiary_category.append(featured_tertiary_category_dict)
        #     featured_category_dict['tertiary_category'] = featured_tertiary_category
        #     featured_category.append(featured_category_dict)
        # print (featured_category)
        # *****************************  Electronic Category content start  ****************************************************



        obj = BaseTemplateHeader(self.request)
        base_template_data = obj.GetHeaderContent()

        context = {
            'base_template_content': base_template_data,

            'mens_banner_image': get_mens_fashion,
            'womens_banner_image': get_womens_fashion,
            'baby_kid_banner_image': get_baby_kid_fashion,
            'mobile_banner_image': get_mobile_fashion,
            'electronic_banner_image': get_electronic_fashion,
            'office_appliance_image': get_office_fashion,
            'banner_1': banner_1,
            'banner_2': banner_2,
            'banner_3': banner_3,
            'banner_4': banner_4,
            'banner_5': banner_5,
            'banner_6': banner_6,
            'banner_right': banner_right,

            'exclusive_category': exclusive_category,

            'offer_products': offer_products,

            'featured_category': featured_category
        }

        return context
