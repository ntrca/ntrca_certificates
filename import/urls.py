
from django.urls import path

from .views import UpdateDistrict, UpdateResult

urlpatterns = [
    path('update/', UpdateDistrict.as_view(), name="update"),
    path('result/', UpdateResult.as_view(), name="result"),
]
