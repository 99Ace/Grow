from django import forms
from .models import Invoice
from cloudinary.forms import CloudinaryJsFileField


class DateInput(forms.DateInput):
    input_type = 'date'

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%d"
        super().__init__(**kwargs)


class NewInvoice(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = (
            'invoice',
            'invoice_reference',
            'car_plate',
            'accounts_receivables',
            'balance',
            'accounts_payable',
            'inv_date',
            'cover'
        )
        widgets = {
            'inv_date': DateInput()
        }
        labels = {
            'invoice': "Invoice for",
            'invoice_reference': "Reference Number (if any)",
            'car_plate': "Car plate (if applicable)",
            'accounts_receivables': "Amount",
            'balance': "Credit / Debit",
            'accounts_payable': "Supplier",
            'inv_date': "Invoice Date",
        }
    cover = CloudinaryJsFileField()


class EditInvoice(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = (
            'invoice',
            'invoice_reference',
            'car_plate',
            'accounts_receivables',
            'balance',
            'accounts_payable',
            'inv_date',
        )
        widgets = {
            'inv_date': DateInput()
        }
        labels = {
            'invoice': "Invoice for",
            'invoice_reference': "Reference Number (if any)",
            'car_plate': "Car plate (if applicable)",
            'accounts_receivables': "Amount",
            'balance': "Credit / Debit",
            'accounts_payable': "Supplier",
            'inv_date': "Invoice Date",
        }
