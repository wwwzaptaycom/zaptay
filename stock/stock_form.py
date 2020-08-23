from django import forms

class StockEntryForm(forms.Form):
    product_id = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'product_id', 'readonly': 'readonly'}),
            error_messages={'required': 'Product ID Required'})

    stock = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'stock_qty', 'placeholder': 'Stock QTY', 'min': 0}),
            error_messages={'required': 'Stock Qty Required'})

    main_price = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'main_price', 'placeholder': 'Main Price', 'min': "0.00", 'step': "0.01"}),
            error_messages={'required': 'Main Price Required'})

    offer_price = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'offer_price', 'placeholder': 'Offer Price', 'min': "0.00", 'step': "0.01"}),
            error_messages={'required': 'Offer Price Required'})

    # extra_offer = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'extra_offer', 'placeholder': 'Main Price'}),
    #         error_messages={'required': 'Extra Offer Price Required'})

    purchase = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'purchase', 'placeholder': 'Purchase Price', 'min': "0.00", 'step': "0.01"}),
            error_messages={'required': 'Purchase Price Required'})
