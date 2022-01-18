
from django.contrib import admin
from django.urls import path, include
from cloud_storage.views import get_bucket_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', get_bucket_data, name="get_bucket_data"),
]
