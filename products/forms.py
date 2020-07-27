# Create your models here.
from django import forms



class size_form(forms.Form):

    fitting = [
    ('EU34/UK6', 'EU 34/UK 6'),
    ('EU36/UK8', 'EU 36/UK 8'),
    ('EU38/UK10', 'EU 38/UK 10'),
    ('EU40/UK12', 'EU 40/UK 12'),
    ('EU42/UK14', 'EU 42/UK 14'),
    ('EU44/UK16', 'EU 44/UK 16'),
    ('EU46/UK18', 'EU 46/UK 18'),
]


    right_size = forms.ChoiceField(label='Enter Your Size', choices=fitting, required=False)

    