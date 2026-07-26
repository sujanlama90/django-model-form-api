from django import forms
from .models import *

GENDER_FIELD = (
    ('male', 'Male'),
    ('female', 'Female'),
)

SUBJECT_FIELD = (
    ('django', 'Django'),
    ('python', 'Python'),
    ('database', 'Database'),
    ('mern', 'MERN'),
)

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name' :forms.TextInput(attrs={"class": "form-control"}),
            'age' : forms.NumberInput(attrs={"class": "form-control"}),
            'password' : forms.PasswordInput(attrs={"class": "form-control"}),
            'gender': forms.RadioSelect(choices=GENDER_FIELD),
            'subject' : forms.CheckboxSelectMultiple(choices=SUBJECT_FIELD)
        }