from django.shortcuts import render
from django.views.generic import TemplateView, CreateView,ListView,UpdateView,DeleteView
from .forms import *
from .models import *
# Create your views here.

# class GenericView(TemplateView):
#     template_name='generic/index.html'

class GenericView(ListView):
    model = Detail
    template_name='generic/index.html'
    context_object_name ='data'


class CreateDataView(CreateView):
    template_name = 'generic/forms.html'
    model = Detail
    form_class =   DetailForm 
    success_url = '/generic'

class UpdateDataView(UpdateView):
    template_name = 'generic/update.html'
    model = Detail
    form_class = DetailForm
    success_url = '/generic'

class DeleteDataView(DeleteView):
    template_name = 'generic/delete.html'
    model = Detail
    success_url = '/generic'
    
