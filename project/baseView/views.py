'''views.py
it's types:
1. function based view
2.class based view : view implementing using python class instead of function .
it is used to organized the code occording http method ,reuse , inharitance

CBSv types:
base classed base view/base view (to create classed by yourself)
generic classed base view/generic view(ready to use view:builtin features) '''
from django.shortcuts import render,redirect
from django.views import View
from .models import *
# def baseView(request):
#     return render(request,'baseView.html')

# class ShowView(View):
#     name = 'sujan'
#     def get(self,request):
#         return HttpResponse('hello this is base view')
    
# class ChildView(ShowView):
#     def get(self,request):
#         return HttpResponse(f'hello this is child view {self.name}')

class IndexView(View):
    def get(self,request):
        data = BaseView.objects.all()
        return render(request,'baseView/index.html',{'data':data})
    
    def post(self, request):
        name = request.POST.get('name')
        age = request.POST.get('age')
        BaseView.objects.create(name=name,age=age)
        return redirect('indexview')
    
        