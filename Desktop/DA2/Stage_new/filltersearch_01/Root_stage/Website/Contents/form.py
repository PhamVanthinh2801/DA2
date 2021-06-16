from django import forms
from string import Template
from django.utils.safestring import mark_safe
from django.forms import ImageField
from multiupload.fields import MultiFileField

CHOOSE_SIZE = (
    ('Small', 'Small'),
    ('Medium', 'Medium'),
    ('Large', 'Large'),
)


CHOOSE_COLOR=(
    ('Purple','Purple'),
    ('Red','Red'),
    ('Blue','Blue')
)

PAYMENT_CHOICE = (
    ('Cash', 'Cash'),
    ('Transfermoney', 'Transfermoney'),
    ('Shipcode', 'Shipcode')
)


class PaymentFrom(forms.Form):
    adress=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'123/Quangtrung/12/A','class':'form-control'}),required=False)
    gender=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nam/Nữ','class':'form-control'}),required=False)
    phone=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'123456789','class':'form-control'}),required=False)
    bridday=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'15/02/1995','class':'form-control'}),required=False)
    identify=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'123456789','class':'form-control'}),required=False)
    paymentoption=forms.ChoiceField(widget=forms.RadioSelect,choices=PAYMENT_CHOICE)

class CheckoutFrom(forms.Form):
    adress=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'','class':'form-control'}))
    gender=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nam/Nữ','class':'form-control'}))
    phone=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'','class':'form-control'}))
    bridday=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'','class':'form-control'}))
    identify=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'','class':'form-control'}))

class Choosesize(forms.Form):
    productsize=forms.ChoiceField(
        choices=CHOOSE_SIZE,
        widget=forms.RadioSelect,
        required=True,
        error_messages={'required': 'myRequiredMessage'})

    producColor=forms.ChoiceField(
        choices=CHOOSE_COLOR,
        widget=forms.RadioSelect,
        required=True,
        error_messages={'required': 'myRequiredMessage'})



class Commentform(forms.Form):
    Content=forms.CharField(widget=forms.Textarea(attrs={'placeholder':'','class':'form-control'}))
    Stars=forms.IntegerField(widget= forms.NumberInput(attrs={'placeholder':'','class':'form-control'}))
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}),required=False)
    # image=forms.ImageField()


class AddressForm(forms.Form):
    address=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'','class':'form-control'}))