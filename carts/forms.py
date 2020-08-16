from django import forms



class Snippet(forms.Form):
    cart = forms.BooleanField(
        label='hi',
        initial=False, required=True)