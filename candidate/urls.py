
from django.urls import path

from .views import create_data, ImportCandidate

urlpatterns = [
    path('home/', create_data , name="create_data"),
    path('import/', ImportCandidate.as_view(), name="candidate_import")
]
