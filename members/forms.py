from django import forms
from django.forms import ModelForm
from .models import MembershipNumber, Member

# class MemberModelForm(forms.ModelForm):
#     class Meta:
#         model = Member
#         fields = ('first_name', 'last_name', 'phone', 'email', 'package',
#                   'street', 'city', 'zip_code')

# class MembershipNoForm(forms.ModelForm):
#     class Meta:
#         model = MembershipNumber
#         fields = ('id_number', )

#         widgets = {
#             'id_number':
#             forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Enter Your ID Number',
#                     'name': 'id_number'
#                 }),
#         }


class IdNumberForm(ModelForm):
    class Meta:
        model = MembershipNumber
        fields = ('id_number', 'user')

        widgets = {
            'id_number':
            forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Your ID Number',
                    'name': 'id_number'
                }),
            'user':
            forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'value': "",
                    'type': 'hidden',
                    'id': 'member',
                }),
        }


class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = ('first_name', 'last_name', 'phone', 'email', 'package',
                  'street', 'town', 'city', 'zip_code')

        widgets = {
            'first_name':
            forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name'
            }),
            'last_name':
            forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name'
            }),
            # 'membership_no':
            # forms.TextInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Confirm ID Number'
            # }),
            'email':
            forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'example@thuso.com'
            }),
            'phone':
            forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number'
            }),
            'street':
            forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Street'
            }),
            'town':
            forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Town'
            }),
            'city':
            forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'City'
            }),
            'zip_code':
            forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Postal Code'
            }),
        }
