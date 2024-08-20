from tkinter import Widget

from django import forms

from .models import ContactMe


class ContactMeForm(forms.ModelForm):
    """Form definition for ContactMe."""

    class Meta:
        """Meta definition for ContactMeform."""

        model = ContactMe
        fields = ("name", "email", "phone_number", "message")
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "su nombre"}
            ),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control"}),
            "message": forms.Textarea(attrs={"class": "form-control"}),
        }
