from django import forms
from .models import MainCategory

class AddMainCategoryForm(forms.Form):
    category_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'id': 'exampleInputEmail', 'aria-describedby':"emailHelp", 'placeholder':"Example: Men fashion, Women fashion"}), error_messages={'required': 'Category name required'})


def get_main_category():
    main_category = MainCategory.objects.values('category_id', 'main_category_name')
    # print (main_category[0].category_id, main_category[0].main_category_name)
    main_cat_list = list()
    for data in main_category:
        cat_data = (data['category_id'], data['main_category_name'])
        main_cat_list.append(cat_data)
    return main_cat_list

class AddSubCategoryForm(forms.Form):
    # FRUIT_CHOICES= [
    # ('orange','Oranges'),
    # ('cantaloupe','Cantaloupes'),
    # ('mango','Mangoes'),
    # ('honeydew','Honeydews'),
    # ]

    CATEGORY_CHOOSE = get_main_category()

    category_list = forms.CharField(label='What is your favorite fruit?', widget=forms.Select(choices=CATEGORY_CHOOSE, attrs={'class': 'my_select_box'}))
    sub_category_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'id': 'exampleInputEmail', 'aria-describedby':"emailHelp", 'placeholder':"Example: Saree, Kurta"}), error_messages={'required': 'Category name required'})
