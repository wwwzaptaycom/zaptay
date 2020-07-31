from django import forms

class ProductForm(forms.Form):

    category_options = [
        ('','Select Category'),
        ('1', '1')
    ]

    sub_category_options = [
        ('','Select Sub Category'),
        ('1', '1')
    ]

    ter_category_option = [
        ('', 'Tertiary Category'),
        ('1', '1')
    ]

    color_choice = [
        ('', 'Select Color'),
        ('1', '1')
    ]

    size_choice = [
        ('', 'Select Size'),
        ('1', '1')
    ]

    made_in_choice = [
        ('', 'Select Made In'),
        ('1', '1')
    ]

    product_title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'inputAddress', 'placeholder': 'Title of the product'}))
    mrp_price = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'mrp', 'placeholder': 'Main Price', 'min': 0}))
    sell_price = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'sell', 'placeholder': 'Offer Price', 'min': 0}))
    extra_discount = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'extra_disc', 'placeholder': 'Extra Offer Price', 'min': 0}))
    category = forms.CharField(required=True, widget=forms.Select(choices=category_options, attrs={'class': 'form-control', 'id': 'category'}))
    sub_cateegory = forms.CharField(required=True, widget=forms.Select(choices=sub_category_options, attrs={'class': 'form-control', 'id': 'sub_category'}))
    tertiary = forms.CharField(required=True, widget=forms.Select(choices=ter_category_option, attrs={'class': 'form-control', 'id': 'ter_category'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'descrip', 'rows': 9, 'placeholder': 'Product description'}))
    color = forms.CharField(required=True, widget=forms.Select(choices=color_choice, attrs={'class': 'custom-select my-1 mr-sm-2', 'id': 'color'}))
    size = forms.CharField(required=True, widget=forms.Select(choices=size_choice, attrs={'class': 'custom-select my-1 mr-sm-2', 'id': 'size'}))
    made_in = forms.CharField(required=True, widget=forms.Select(choices=made_in_choice, attrs={'class': 'custom-select my-1 mr-sm-2', 'id': 'made_in'}))
    # weekly_dreals = forms.BooleanField()
    weekly_dreals = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'custom-control-input', 'id': 'weely_dreals'}))
    top_offer = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'custom-control-input', 'id': 'top_offer'}))
    free_shiping = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'custom-control-input', 'id': 'free_shiping'}))
    return_product = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'custom-control-input', 'id': 'return'}))
    cod = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'custom-control-input', 'id': 'cod'}))
    youtube = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'youtube', 'placeholder':'Youtube link'}))

    product_image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'custom-file-input', 'id': 'product_img', 'multiple': 'multiple'}))
