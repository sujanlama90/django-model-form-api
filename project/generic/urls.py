from django.urls import path
from .views import *
urlpatterns = [
    # path('',GenericView.as_view(template_name='generic/forms.html'), name='gview'),
    path('',GenericView.as_view(), name='gview'),
    path('create/',CreateDataView.as_view(),name='create'),
    path('update/<pk>',UpdateDataView.as_view(),name='update'),
    path('delete/<pk>',DeleteDataView.as_view(),name='delete')
]
 