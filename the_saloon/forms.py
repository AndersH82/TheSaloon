from django import forms
from .models import Shout

class ShoutForm(forms.ModelForm):
    body = forms.CharField(required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Enter your Shouts in The Saloon!",
                "class":"form-control",
                }
                ),
                label="",
        )
    
    class Meta:
        model = Shout
        exclude = ("user",)