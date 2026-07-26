from django import forms

GENDER_FIELD = (
    ('male','male'),
    ('female','female')
)

SUBJECT_FIELD =(
    ('django','django'),
    ('python','python'),
    ('database','database'),
    ('Mern','Mern')
    
)
class StudentForm(forms.Form):
    name = forms.CharField(
        label="Full Name",
        initial="Sujan Lama",
        strip=True,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    age = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    
    gender_field = forms.ChoiceField(
        choices=GENDER_FIELD,widget=forms.RadioSelect)
    
    subject = forms.MultipleChoiceField(choices=SUBJECT_FIELD,widget=forms.CheckboxSelectMultiple)