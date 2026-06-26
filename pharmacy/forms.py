from django import forms
from .models import Medicine
from .models import Medicine, Supplier,Bill

class MedicineForm(forms.ModelForm):


    class Meta:
        model = Medicine
        fields = '__all__'

        widgets = {

            'medicine_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'category': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'quantity': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),

        }

class SupplierForm(forms.ModelForm):

    class Meta:
        model = Supplier
        fields = '__all__'

        widgets = {

            'supplier_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'contact': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'address': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3
                }
            ),

        }

class BillForm(forms.ModelForm):

    class Meta:
        model = Bill
        fields = ['customer_name']

from django import forms
from .models import StoreProfile


class StoreProfileForm(forms.ModelForm):

    class Meta:
        model = StoreProfile
        fields = "__all__"

        widgets = {
            "store_name": forms.TextInput(attrs={"class": "form-control"}),
            "owner_name": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "gst_number": forms.TextInput(attrs={"class": "form-control"}),
            "address": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }

from .models import Settings

class SettingsForm(forms.ModelForm):

    class Meta:

        model = Settings

        fields = "__all__"

        widgets = {

            "gst_percentage":forms.NumberInput(
                attrs={"class":"form-control"}
            ),

            "low_stock_limit":forms.NumberInput(
                attrs={"class":"form-control"}
            ),

            "currency":forms.TextInput(
                attrs={"class":"form-control"}
            ),

        }