from django import forms
from members.models import Member, Spouse, Family
from django.forms import ModelForm

# class UpdateMemberForm(forms.ModelForm):
#     class Meta:
#         model = Member
#         # fields = '__all__'
#         exclude = ('user', )

STATUS_CHOICES = [
    ('pending', 'pending'),
    ('active', 'active'),
    ('cancelled', 'cancelled'),
]


class UpdateMemberForm(ModelForm):
    class Meta:
        model = Member
        fields = ('first_name', 'last_name', 'status', 'phone', 'email',
                  'package', 'street', 'town', 'city', 'zip_code')

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


class UpdatePendingMemberForm(ModelForm):
    class Meta:
        model = Member
        fields = ('first_name', 'last_name', 'status', 'phone', 'email',
                  'package', 'street', 'town', 'city', 'zip_code')

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


# class UpdatePendingMemberForm(forms.ModelForm):
#     class Meta:
#         model = Member
#         exclude = ('user', )

#         widgets = {
#             'status':
#             forms.Select(choices=STATUS_CHOICES,
#                          attrs={
#                              'class': 'form-select',
#                              'placeholder': 'First Name'
#                          }),
#             'first_name':
#             forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'First Name'
#             }),
#             'last_name':
#             forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Last Name'
#             }),
#             'email':
#             forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'example@thuso.com'
#             }),
#             'phone':
#             forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Phone Number'
#             }),
#             'street':
#             forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Street'
#             }),
#             'town':
#             forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Town'
#             }),
#             'city':
#             forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'City'
#             }),
#             'zip_code':
#             forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Postal Code'
#             }),
#         }


class SpouseForm(forms.ModelForm):
    class Meta:
        model = Spouse
        fields = '__all__'


class FamilyMemberForm(forms.ModelForm):
    class Meta:
        model = Family
        fields = '__all__'