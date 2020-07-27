from django import forms
from category.models import MainCategory
from attribute.models import SubCategory

class CategoryForm(forms.Form):
    category_add_form = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'id': 'exampleInputEmail', 'aria-describedby':"emailHelp", 'placeholder':"Category"}), error_messages={'required': 'Category name required'})

def get_main_category():
    main_category = MainCategory.objects.values('category_id', 'main_category_name')
    # print (main_category[0].category_id, main_category[0].main_category_name)
    main_cat_list = list()
    initial = ('', 'Select category')
    main_cat_list.append(initial)
    for data in main_category:
        cat_data = (data['category_id'], data['main_category_name'])
        main_cat_list.append(cat_data)
    return main_cat_list

class SubcategoryForm(forms.Form):
    # options = [
    #     ('1', '1'),
    #     ('2', '2'),
    # ]


    # forms.ChoiceField(choices=LOCATIONS, required=True )
    # category_list = forms.CharField(label='What is your favorite fruit?', widget=forms.Select(choices=get_main_category(), attrs={'class': 'custom-select'}))
    category_list = forms.ChoiceField(choices=get_main_category(), required=True, widget=forms.Select(choices=get_main_category(), attrs={'class': 'custom-select'}))
    sub_category_add_form = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'aria-describedby':"emailHelp", 'placeholder':"Sub category"}), error_messages={'required': 'Sub Category name required'})

def get_sub_category():
    sub_category = SubCategory.objects.values('sub_category_id', 'sub_category_name')
    # print (main_category[0].category_id, main_category[0].main_category_name)
    sub_cat_list = list()
    initial = ('', 'Select category')
    sub_cat_list.append(initial)
    for data in sub_category:
        cat_data = (data['sub_category_id'], data['sub_category_name'])
        sub_cat_list.append(cat_data)
    return sub_cat_list

class TertiaryCategoryForm(forms.Form):
    options = [
        ('1', '1'),
        ('2', '2'),
    ]

    sub_category_list = forms.CharField(label='What is your favorite fruit?', widget=forms.Select(choices=get_sub_category(), attrs={'class': 'custom-select'}))
    tert_category_add_form = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'aria-describedby':"emailHelp", 'placeholder':"Category"}), error_messages={'required': 'Sub Category name required'})
