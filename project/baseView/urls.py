from django.urls import path
from .views import *
urlpatterns = [
#     path('',baseView,name='baseView'),
#     path('show/',ShowView.as_view(),name='showview'),
#     path('child/',ChildView.as_view())
      path('',IndexView.as_view(),name='indexview')
 ]
