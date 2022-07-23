
from django.urls import path
from .views import NtrcaHomeView, NtrcaDateBoard, NtrcaCreateResult, UpdateCandidate
from .export import export_users_xls

urlpatterns = [
    path('', NtrcaHomeView.as_view(), name="ntrca_result"),
    path('create-date-doard/', NtrcaDateBoard.as_view(), name="ntrca_search_date"),
    path(
        'result-create/', NtrcaCreateResult.as_view(), 
        name="ntrca_result_create"
        ),
    path(
        'result-update/<int:pk>/', UpdateCandidate.as_view(), 
        name="ntrca_update"
        ),

    path('export-data/', export_users_xls, name="export_users_xls"),
    # path('get-data/', insert_data_to_mysql, name= "insert_data"),
]
