
from django.urls import path
from .views import (
    NtrcaInputDistrict, NTRCACirtificateDownloadView,
    NtrcaSingleData, NtrcaDistrictDistribution, update_data,
    NTRCADuplicateCertificatePrintView, DashboardView
)

urlpatterns = [
    path('', DashboardView.as_view(), name="dashboard"),
    path('update/data', update_data, name="update_data"),
    path(
        'ntrca/district/<int:pk>/', NtrcaInputDistrict.as_view(),
        name="ntrca_district"
    ),
    path(
        'ntrca/cirtificate/download/<int:pk>/',
        NTRCACirtificateDownloadView.as_view(),
        name="ntrca_cirtificate_download"
    ),
    path('ntrca/single/data/<int:pk>/', NtrcaSingleData.as_view(),
    name="ntrca_single_data"),
    path(
        'ntrca/district/distribution/<int:pk>/',
        NtrcaDistrictDistribution.as_view(), 
        name="ntrca_district_distribution"
    ),
    path('ntrca/single/duplicate/certificate/', 
        NTRCADuplicateCertificatePrintView.as_view(), 
        name="ntrca_duplicate_certificate"
    ),
]
