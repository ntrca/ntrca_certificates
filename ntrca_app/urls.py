
from django.urls import path
from .views import (
    NTRCACirtificateView, NtrcaInputDistrict, NTRCACirtificateDownloadView,
    NtrcaSingleData, NtrcaDistrictDistribution
)

urlpatterns = [
    path('', NtrcaInputDistrict.as_view(), name="ntrca_district"),
    path('ntrca/cirtificate/download/', NTRCACirtificateDownloadView.as_view(),
    name="ntrca_cirtificate_download"),
    path('ntrca/single/data/', NtrcaSingleData.as_view(),
    name="ntrca_single_data"),
    path('ntrca/cirtificateView/', NTRCACirtificateView.as_view(), 
        name="ntrca_cirtificateView"),
    path('ntrca/district/distribution/', NtrcaDistrictDistribution.as_view(), 
        name="ntrca_district_distribution"),
]
