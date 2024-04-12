# forms.py
from django import forms


class HospitalCostPredictionForm(forms.Form):
    MARTIAL_STATUS_CHOICES = [
        ('unmarried', 'Unmarried'),
        ('married', 'Married'),
    ]
    AGE_CHOICES = [(i, str(i)) for i in range(1, 101)]
    COMPLAINT_CHOICES = [
        (0, 'ACHD'),
        (1, 'CAD'),
        (5, 'NONE'),
        (2, 'OS-ASD'),
        (4, 'OTHER'),
        (3, 'RHD'),
    ]

    martial_status = forms.ChoiceField(
        label='What is your Marital status?',
        choices=MARTIAL_STATUS_CHOICES,
        widget=forms.RadioSelect
    )
    age = forms.IntegerField(label='Age:', widget=forms.NumberInput(attrs={'min': 1, 'max': 100}))
    complaint = forms.ChoiceField(
        label='Key Complaints',
        choices=COMPLAINT_CHOICES,
        widget=forms.Select(attrs={'required': True})
    )
    weight = forms.DecimalField(label='Weight:', widget=forms.NumberInput(attrs={'min': 0}), required=True)
    height = forms.DecimalField(label='Height:', widget=forms.NumberInput(attrs={'min': 0, 'max': 243}), required=True)

