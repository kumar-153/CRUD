from django import forms 
from .models import Register

class Register(forms.ModelForm):
    class Meta:
        model = Register
        fields = [ 
            "medical_name", 
            "phone_name",
            "phone_no",
            "address",
        ] 