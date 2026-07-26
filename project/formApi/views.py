from django.shortcuts import render,redirect
from .form import *
from .models import *


def home(request):
    form = StudentForm()

    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            password = form.cleaned_data['password']
            gender = form.cleaned_data['gender_field']   
            subject = form.cleaned_data['subject']       

            Students.objects.create(
                name=name,
                age=age,
                password=password,
                gender=gender,
                subject=subject 
            )

            return redirect('home')

    return render(request, 'home.html', {'form': form})