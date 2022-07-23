
from django.urls import path
from .views import ResultHomeView, DateBoardView, MarkesEntry, UpdateCandidate
from .export import export_users_xls

urlpatterns = [
    path('result/home/<int:exam_pk>/', ResultHomeView.as_view(), name="result_home"),
    path('search/page/<int:pk>/', DateBoardView.as_view(), name="ntrca_search_date"),
    path(
        'result-create/<int:pk>/', MarkesEntry.as_view(), 
        name="markes_entry"
        ),
    path(
        'result-update/<int:pk>/', UpdateCandidate.as_view(), 
        name="ntrca_update"
        ),

    path('export-data/', export_users_xls, name="export_users_xls"),
    # path('get-data/', insert_data_to_mysql, name= "insert_data"),
]
