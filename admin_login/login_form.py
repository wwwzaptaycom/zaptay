from django import forms

import re

class LoginForm(forms.Form):
    email_id = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control form-control-user', 'id': 'exampleInputEmail', 'aria-describedby':"emailHelp", 'placeholder':"Enter Email Address..."}), error_messages={'required': 'Email Id Required'})
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control form-control-user", 'id': "exampleInputPassword", 'placeholder': "Password"}), error_messages={'required': 'Password Required'})

    def clean(self):
        email = self.cleaned_data.get('email_id')
        pwd = self.cleaned_data.get('password')

        # email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        email_regex = '^[a-z0-9.]+[@]\w+[.]\w{2,3}$'
        if email != None and re.search(email_regex, email) == None:
            raise forms.ValidationError(
                ({'email_id': ["Invalid Email"]})
            )
        return True


        # first_name = forms.CharField(min_length=4, widget=forms.TextInput(attrs={'class': 'textbox', 'autocomplete': 'off', 'placeholder': "Enter first name"}), error_messages={'required': 'First name required', 'min_length': 'First name length error'})
