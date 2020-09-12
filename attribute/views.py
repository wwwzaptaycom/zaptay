from django.contrib import messages

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, TemplateView, FormView

from admin_login.models import zaptayAdmin

from .attribute_forms import CategoryForm, SubcategoryForm, TertiaryCategoryForm, ColorForm, SizeForm, SourceForm, SameDayPincodeForm, NextDayPincodeForm

from category.models import MainCategory
from attribute.models import SubCategory, TertiaryCategory, Colour, Size, Source, SameDayDelivary, NextDayDelivary

from django.db.models import Subquery

# Create your views here.

class AttributeList(FormView):
    template_name = 'admin_template/attributes.html'
    # form_class = CategoryForm
    category_form_class = CategoryForm
    sub_category_form_class = SubcategoryForm
    teri_category_class = TertiaryCategoryForm
    color_class = ColorForm
    size_class = SizeForm
    source_class = SourceForm
    same_day_pincode_class = SameDayPincodeForm
    next_day_pincode_class = NextDayPincodeForm

    def dispatch(self, request, *args, **kwargs):
        try:
            resp = request.session['admin_email_id']
            return super(AttributeList, self).dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)
            # return redirect('/site-admin/login')
            return redirect('admin_login:admin_loginpage')

    def get_context_data(self, **kwargs):
        context = dict()
        get_name = zaptayAdmin.objects.all().get(email_id=self.request.session['admin_email_id'])
        category_list = MainCategory.objects.all()
        sub_category_list = SubCategory.objects.all()
        ter_caregory_list = TertiaryCategory.objects.all()
        color_list = Colour.objects.all()
        size_list = Size.objects.all()
        source_list = Source.objects.all()
        same_day_delivary_pin_list = SameDayDelivary.objects.all()
        next_day_delivary_pin_list = NextDayDelivary.objects.all()

        # print (sub_category_list[0].category_id.main_category_name) # Worked
        # Teritory category with sub category and category
        ter_caregory_list_2 = list()
        for category in category_list:
            print (category.main_category_name)
            get_sub_category = SubCategory.objects.filter(category_id=category)
            for sub_category in get_sub_category:
                print ("\t"+sub_category.sub_category_name)
                get_tertiary_category = TertiaryCategory.objects.filter(sub_category_id=sub_category)
                for tertiary_category in get_tertiary_category:
                    print ("\t\t"+tertiary_category.ter_category_name)


        context = {
            "page_name": "attribute",
            "admin_name": get_name.admin_f_name+" "+get_name.admin_f_name,
            "category_list": category_list,
            "sub_category_list": sub_category_list,
            "ter_category_list": ter_caregory_list,
            "color_list": color_list,
            "size_list": size_list,
            "source_list": source_list,
            "same_day_pin_list": same_day_delivary_pin_list,
            "next_day_pin_list": next_day_delivary_pin_list}

        context['category_form'] = self.category_form_class
        context['sub_category_form'] = self.sub_category_form_class
        context['tertia_form'] = self.teri_category_class
        context['color_form'] = self.color_class
        context['size_form'] = self.size_class
        context['source_form'] = self.source_class
        context['same_day_pincode_form'] = self.same_day_pincode_class
        context['next_day_pincode_form'] = self.next_day_pincode_class
        return context

    def post(self, request, *args, **kwargs):
        if 'category_add_form' in request.POST:
            category_form = CategoryForm(request.POST)

            if category_form.is_valid():
                category_name = request.POST['category_add_form'].lower()
                admin_id = zaptayAdmin.objects.all().get(email_id=request.session.get('admin_email_id'))
                insert_que = MainCategory(main_category_name = category_name, added_by = admin_id)
                insert_que.save()
                messages.success(request, "Catagory added", extra_tags='category')
            else:
                messages.error(request, "All fields mentetory", extra_tags='category')

        if 'sub_category_add_form' in request.POST:
            sub_category_from = SubcategoryForm(request.POST)

            if sub_category_from.is_valid():
                main_category_id = request.POST['category_list']
                sub_category_name = request.POST['sub_category_add_form']

                admin_id = zaptayAdmin.objects.all().get(email_id=request.session.get('admin_email_id'))
                get_category_id = MainCategory.objects.get(pk=main_category_id)
                insert_que = SubCategory(sub_category_name=sub_category_name, added_by=admin_id, category_id=get_category_id)
                insert_que.save()
                messages.success(request, "Sub catagory added", extra_tags='sub_category')
                # print (main_category_id, sub_category_name, get_category_id)
            else:
                # select_category = request.POST['']
                messages.error(request, "All fields mentetory", extra_tags='sub_category')

        if 'tert_category_add_form' in request.POST:
            sub_category_from = TertiaryCategoryForm(request.POST)

            if sub_category_from.is_valid():
                sub_category_id = request.POST['sub_category_list']
                tert_category_name = request.POST['tert_category_add_form']

                admin_id = zaptayAdmin.objects.all().get(email_id=request.session.get('admin_email_id'))
                get_sub_category = SubCategory.objects.get(pk=sub_category_id)

                insert_que = TertiaryCategory(ter_category_name=tert_category_name, added_by=admin_id, sub_category_id=get_sub_category)
                insert_que.save()
                messages.success(request, "Tertiary catagory added", extra_tags='terriary_category')
            else:
                messages.error(request, "All fields mentetory", extra_tags='terriary_category')

        if 'color_add_form' in request.POST:
            color_from = ColorForm(request.POST)

            if color_from.is_valid():
                color_name = request.POST['color_add_form'].lower()

                admin_id = zaptayAdmin.objects.all().get(email_id=request.session.get('admin_email_id'))

                insert_que = Colour(color_name=color_name, added_by=admin_id)
                insert_que.save()
                messages.success(request, "Color added", extra_tags='colour')
            else:
                messages.error(request, "All fields mentetory", extra_tags='colour')

        if 'size_add_form' in request.POST:
            size_from = SizeForm(request.POST)

            if size_from.is_valid():
                size = request.POST['size_add_form'].lower()

                admin_id = zaptayAdmin.objects.all().get(email_id=request.session.get('admin_email_id'))

                insert_que = Size(size_name=size, added_by=admin_id)
                insert_que.save()
                messages.success(request, "Size added", extra_tags='size')
            else:
                messages.error(request, "All fields mentetory", extra_tags='size')

        if 'source_add_form' in request.POST:
            size_from = SourceForm(request.POST)

            if size_from.is_valid():
                source = request.POST['source_add_form'].lower()

                admin_id = zaptayAdmin.objects.all().get(email_id=request.session.get('admin_email_id'))

                insert_que = Source(source_name=source, added_by=admin_id)
                insert_que.save()
                messages.success(request, "Source added", extra_tags='source')
            else:
                messages.error(request, "All fields mentetory", extra_tags='source')

        if 'same_day_pin_add_form' in request.POST:
            same_day_pin_form = SameDayPincodeForm(request.POST)

            if same_day_pin_form.is_valid():
                pin_code_no = request.POST['same_day_pin_add_form']

                admin_id = zaptayAdmin.objects.all().get(email_id=request.session.get('admin_email_id'))

                insert_que = SameDayDelivary(pincode=pin_code_no, added_by=admin_id)
                insert_que.save()
                messages.success(request, "pincode added", extra_tags='same_day_pin')
            else:
                messages.error(request, "All fields mentetory", extra_tags='same_day_pin')

        if 'next_day_pin_add_form' in request.POST:
            next_day_pin_form = NextDayPincodeForm(request.POST)

            if next_day_pin_form.is_valid():
                pin_code_no = request.POST['next_day_pin_add_form']

                admin_id = zaptayAdmin.objects.all().get(email_id=request.session.get('admin_email_id'))

                insert_que = NextDayDelivary(pincode=pin_code_no, added_by=admin_id)
                insert_que.save()
                messages.success(request, "pincode added", extra_tags='next_day_pin')
            else:
                messages.error(request, "All fields mentetory", extra_tags='next_day_pin')

        return render(request, self.template_name, self.get_context_data())

    def form_invalid(self, form):
        context = self.get_context_data(task_form=form)
        context['error'] = form
        print (context)
        return self.render_to_response(context)


# Modify data runtime

from django.http import JsonResponse
def SendCategoryData(request):

    category_dict = dict()
    category_arr = list()

    category_list = MainCategory.objects.all()
    for i in category_list:
        category_arr.append([i.category_id , i.main_category_name])
        # print (i.category_id, i.main_category_name)
    category_dict['data'] = category_arr
    # print (category_dict)

    responseData = {
        'id': 4,
        'name': 'Test Response',
        'roles' : ['Admin','User']
    }
    return JsonResponse(category_dict)

def SendSubCategoryData(request):

    category_dict = dict()
    category_arr = list()

    category_list = SubCategory.objects.all()
    for i in category_list:
        category_arr.append([i.sub_category_id , i.sub_category_name])
    category_dict['data'] = category_arr

    return JsonResponse(category_dict)

def DeleteAttrinutsData(request):
    attribute_id = request.POST['attribute_id']
    attribut_attribute_type = request.POST['attribute_type']

    # print (attribute_id, attribut_attribute_type)

    if attribut_attribute_type == 'category':
        get_data = MainCategory.objects.get(pk=attribute_id)
        get_data.delete()

    if attribut_attribute_type == 'sub_category':
        get_data = SubCategory.objects.get(pk=attribute_id)
        get_data.delete()

    if attribut_attribute_type == 'tertiary_category':
        get_data = TertiaryCategory.objects.get(pk=attribute_id)
        get_data.delete()

    if attribut_attribute_type == 'color':
        get_data = Colour.objects.get(pk=attribute_id)
        get_data.delete()

    if attribut_attribute_type == 'size':
        get_data = Size.objects.get(pk=attribute_id)
        get_data.delete()

    if attribut_attribute_type == 'source':
        get_data = Source.objects.get(pk=attribute_id)
        get_data.delete()

    if attribut_attribute_type == 'same_day_pin':
        get_data = SameDayDelivary.objects.get(pk=attribute_id)
        get_data.delete()

    if attribut_attribute_type == 'next_day_pin':
        get_data = NextDayDelivary.objects.get(pk=attribute_id)
        get_data.delete()

    resp = {
        "response": 'success'
    }

    return JsonResponse(resp)


def SendSortSubCategory(request):
    try:
        category_id = request.GET['category_id']

        category_dict = dict()
        category_arr = list()

        category_list = SubCategory.objects.all().filter(category_id=category_id)
        for i in category_list:
            category_arr.append([i.sub_category_id , i.sub_category_name])
        category_dict['data'] = category_arr

        return JsonResponse(category_dict)

    except Exception as e:
        print ("*********************************************************************************************************************************")
        print ("Error in ajax", e)
        print ("*********************************************************************************************************************************")

        resp = {
            "response": 'Failed'
        }

        return JsonResponse(resp)

def TertiarySubCategory(request):
    try:
        sub_category_id = request.GET['sub_category_id']

        category_dict = dict()
        category_arr = list()

        category_list = TertiaryCategory.objects.all().filter(sub_category_id=sub_category_id)
        for i in category_list:
            category_arr.append([i.ter_category_id , i.ter_category_name])
        category_dict['data'] = category_arr

        return JsonResponse(category_dict)

    except Exception as e:
        print ("*********************************************************************************************************************************")
        print ("Error in ajax", e)
        print ("*********************************************************************************************************************************")

        resp = {
            "response": 'Failed'
        }

        return JsonResponse(resp)

def GetAllColors(request):
    try:
        category_dict = dict()
        category_arr = list()

        category_list = Colour.objects.all()
        for i in category_list:
            category_arr.append([i.color_id , i.color_name])
        category_dict['data'] = category_arr

        return JsonResponse(category_dict)

    except Exception as e:
        print ("*********************************************************************************************************************************")
        print ("Error in ajax", e)
        print ("*********************************************************************************************************************************")

        resp = {
            "response": 'Failed'
        }

        return JsonResponse(resp)

def GetAllSize(request):
    try:
        category_dict = dict()
        category_arr = list()

        category_list = Size.objects.all()
        for i in category_list:
            category_arr.append([i.size_id , i.size_name])
        category_dict['data'] = category_arr

        return JsonResponse(category_dict)

    except Exception as e:
        print ("*********************************************************************************************************************************")
        print ("Error in ajax", e)
        print ("*********************************************************************************************************************************")

        resp = {
            "response": 'Failed'
        }

        return JsonResponse(resp)

def GetAllMadeIn(request):
    try:
        category_dict = dict()
        category_arr = list()

        category_list = Source.objects.all()
        for i in category_list:
            category_arr.append([i.source_id , i.source_name])
        category_dict['data'] = category_arr

        return JsonResponse(category_dict)

    except Exception as e:
        print ("*********************************************************************************************************************************")
        print ("Error in ajax", e)
        print ("*********************************************************************************************************************************")

        resp = {
            "response": 'Failed'
        }

        return JsonResponse(resp)

def GetSubCategoryDetails(request):
    category_type = request.GET['category_type']
    sub_category = request.GET['sub_category_id']

    category_dict = dict()
    category_arr = list()

    # category_list = MainCategory.objects.filter(category_id__in=Subquery(SubCategory.objects.all().filter(sub_category_id=sub_category_id).values('category_id')))
    # print (category_list[0].main_category_name)

    if category_type != "tertiary_category":
        category_list = SubCategory.objects.all().filter(sub_category_id=sub_category).values('sub_category_id', 'sub_category_name', 'sub_category_image')
        for i in category_list:
            # category_arr.append([i.sub_category_id , i.sub_category_name])
            category_dict['sub_category_id'] = i['sub_category_id'];
            category_dict['sub_category_name'] = i['sub_category_name'].replace("_", " ");
            category_dict['sub_category_image'] = i['sub_category_image'];
        category_dict['data'] = category_arr
    else:
        category_list = TertiaryCategory.objects.all().filter(ter_category_id=sub_category).values('ter_category_id', 'ter_category_name', 'tertiary_category_image')
        for i in category_list:
            # category_arr.append([i.sub_category_id , i.sub_category_name])
            category_dict['sub_category_id'] = i['ter_category_id'];
            category_dict['sub_category_name'] = i['ter_category_name'].replace("_", " ");
            category_dict['sub_category_image'] = i['tertiary_category_image'];
        category_dict['data'] = category_arr

    resp = {
        "response": 'Failed'
    }
    return JsonResponse(category_dict)


# AJAX Image Upload
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def AjaxImageUpload(request):
    if 'sub_category_image' in request.FILES:
        sub_category_id = request.POST['sub_category_id']
        sub_category_name = request.POST['sub_category_name']
        sub_category_image = request.FILES['sub_category_image']
        sub_category_type = request.POST['sub_category_type']
        # print (sub_category_id,sub_category_name,sub_category_image.name)
        if sub_category_type == "tertiary_category":
            fs = FileSystemStorage()
            image_title = sub_category_name+"."+sub_category_image.name.split('.')[-1]
            image_title = image_title.replace(" ", "")
            upload_image = fs.save("tertiary_category/images/"+image_title, sub_category_image)
            img_url = fs.url(upload_image)
            mod_image_name = img_url.split("/")[-1]
            image_path = 'tertiary_category/images/'+mod_image_name
            # print (image_path)

            sub_category_details = TertiaryCategory.objects.filter(ter_category_id=sub_category_id)
            if sub_category_details[0].tertiary_category_image != "":
                os.remove('media/'+str(sub_category_details[0].tertiary_category_image))
                sub_category_details.update(tertiary_category_image = image_path)
            else:
                sub_category_details.update(tertiary_category_image = image_path)
        else:
            fs = FileSystemStorage()
            image_title = sub_category_name+"."+sub_category_image.name.split('.')[-1]
            image_title = image_title.replace(" ", "")
            upload_image = fs.save("sub_category/images/"+image_title, sub_category_image)
            img_url = fs.url(upload_image)
            mod_image_name = img_url.split("/")[-1]
            image_path = 'sub_category/images/'+mod_image_name
            # print (image_path)

            sub_category_details = SubCategory.objects.filter(sub_category_id=sub_category_id)
            if sub_category_details[0].sub_category_image != "":
                os.remove('media/'+str(sub_category_details[0].sub_category_image))
                sub_category_details.update(sub_category_image = image_path)
            else:
                sub_category_details.update(sub_category_image = image_path)
        resp = {
            "response": 'success'
        }
        return JsonResponse(resp)

    resp = {
        "response": 'Failed'
    }
    return JsonResponse(resp)
