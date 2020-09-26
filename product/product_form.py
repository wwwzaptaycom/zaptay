from django import forms

class ProductForm(forms.Form):

    category_options = [
        ('','Select Category'),
        ('', '1')
    ]

    sub_category_options = [
        ('','Select Sub Category'),
        ('', 'Select category first')
    ]

    ter_category_option = [
        ('', 'Tertiary Category'),
        ('', 'Select sub category first')
    ]

    under_ter_category_option = [
        ('', 'Under Tertiary Category'),
        ('', 'Select tertiary category first')
    ]

    brand_choice = [
        ('', 'Select Brand'),
        ('', 'No brand')
    ]

    color_choice = [
        ('', 'Select Color'),
        ('', 'No color fetch')
    ]

    size_choice = [
        ('', 'Select Size'),
        ('', 'No size fetch')
    ]

    made_in_choice = [
        ('', 'Select Made In'),
        ('', 'No made by fetch')
    ]

    product_title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'inputAddress', 'placeholder': 'Title of the product'}), error_messages={'required': 'Product Title Required'})
    # main_price = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'mrp', 'placeholder': 'Main Price', 'min': 0}), error_messages={'required': 'Main Price Required'})
    # offer_price = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'sell', 'placeholder': 'Offer Price', 'min': 0}), error_messages={'required': 'Offer Price Required'})
    # extra_price = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'extra_disc', 'placeholder': 'Extra Offer Price', 'min': 0}), error_messages={'required': 'Extra Price Required'})
    # purchase_price = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'purchase_price', 'placeholder': 'Purchase Price', 'min': 0}), error_messages={'required': 'Purchase Price Required'})
    category = forms.CharField(required=True, widget=forms.Select(choices=category_options, attrs={'class': 'form-control', 'id': 'category'}), error_messages={'required': 'Category Required'})
    sub_cateegory = forms.CharField(required=True, widget=forms.Select(choices=sub_category_options, attrs={'class': 'form-control', 'id': 'sub_category'}), error_messages={'required': 'Sub Category Required'})
    tertiary = forms.CharField(required=False, widget=forms.Select(choices=ter_category_option, attrs={'class': 'form-control', 'id': 'ter_category'}))
    under_tertiary = forms.CharField(required=False, widget=forms.Select(choices=under_ter_category_option, attrs={'class': 'form-control', 'id': 'under_ter_category'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'descrip', 'rows': 11, 'placeholder': 'Product description'}))
    brand = forms.CharField(required=True, widget=forms.Select(choices=brand_choice, attrs={'class': 'custom-select my-1 mr-sm-2', 'id': 'brand'}), error_messages={'required': 'Brand Required'})
    color = forms.CharField(required=True, widget=forms.Select(choices=color_choice, attrs={'class': 'custom-select my-1 mr-sm-2', 'id': 'color'}), error_messages={'required': 'Color Required'})
    size = forms.CharField(required=False, widget=forms.Select(choices=size_choice, attrs={'class': 'custom-select my-1 mr-sm-2', 'id': 'size'}))
    made_in = forms.CharField(required=True, widget=forms.Select(choices=made_in_choice, attrs={'class': 'custom-select my-1 mr-sm-2', 'id': 'made_in'}), error_messages={'required': 'Made In Required'})
    seller = forms.CharField(required=True, widget=forms.Select(attrs={'class': 'custom-select my-1 mr-sm-2', 'id': 'seller'}), error_messages={'required': 'Seller Required'})
    # stock_entry = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'stock', 'placeholder': 'Stock Entry', 'min': 0}), error_messages={'required': 'Purchase Price Required'})
    # weekly_dreals = forms.BooleanField()

    same_day_delivary_check = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'custom-control-input', 'id': 'same_day_delivary'}))
    same_day_delivary_price = forms.CharField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'inputAddress', 'placeholder': 'Price', 'min': 0}))
    next_day_delivary_check = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'custom-control-input', 'id': 'next_day_delivary'}))
    next_day_delivary_price = forms.CharField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'inputAddress', 'placeholder': 'Price', 'min': 0}))
    customize_delivary_check = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'custom-control-input', 'id': 'customize_day_delivary'}))
    customize_delivary_day = forms.CharField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'inputAddress', 'placeholder': 'Add Day', 'min': 0}))
    customize_delivary_price = forms.CharField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'inputAddress', 'placeholder': 'Price', 'min': 0}))

    weekly_dreals = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'custom-control-input', 'id': 'weely_dreals'}))
    top_offer = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'custom-control-input', 'id': 'top_offer'}))
    # free_shiping = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'custom-control-input', 'id': 'free_shiping'}))
    return_product = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'custom-control-input', 'id': 'return'}))
    cod = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'custom-control-input', 'id': 'cod'}))
    youtube = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'youtube', 'placeholder':'Youtube link'}))

    product_image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'custom-file-input', 'id': 'product_img', 'multiple': 'multiple'}))

    def clean(self):
        product_desc = self.cleaned_data.get('description')

        if product_desc == "" or len(product_desc) < 5:
            print("Error")
            raise forms.ValidationError(
                ({'description': ["Product Description Required"]})
            )
        return True
