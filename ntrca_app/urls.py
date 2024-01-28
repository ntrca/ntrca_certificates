
from django.urls import path
from .views import (
    NtrcaInputDistrict, NTRCACirtificateDownloadView,
    NtrcaSingleData, NtrcaDistrictDistribution, update_data,
    NTRCADuplicateCertificatePrintView, DashboardView,
    update_result, update_cirtificate_to_candidate, UpdateRegistration
)

urlpatterns = [
    path('', DashboardView.as_view(), name="dashboard"),
    path('update/data/', update_data, name="update_data"),
    path('update/result/', update_result, name="update_result"),
    path('update/cirtificate/to/candidate/', update_cirtificate_to_candidate, name="update_cirtificate_to_candidate"),
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
    path('ntrca/single/duplicate/certificate/<int:pk>/', 
        NTRCADuplicateCertificatePrintView.as_view(), 
        name="ntrca_duplicate_certificate"
    ),

    # Update registration
    
    path('UpdateRegistration/', UpdateRegistration.as_view(), name="UpdateRegistration"
    ),
]
