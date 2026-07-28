from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('formApi.urls')),
    path('modelapi/',include('modelApi.urls')),
    path('baseview/',include('baseView.urls')),
    path('generic/',include('generic.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
