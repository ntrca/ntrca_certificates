
from django.urls import path

from .views import UpdateDistrict, UpdateResult, delete_cer

urlpatterns = [
    path('update/', UpdateDistrict.as_view(), name="update"),
    path('result/', UpdateResult.as_view(), name="result"),
    path('delete/', delete_cer, name="delete_cer"),
]
