import django_filters
from .models import NtrcaResult

class CandidateFilter(django_filters.FilterSet):
    subject_code = django_filters.CharFilter(lookup_expr='iexact')
    interview_date = django_filters.CharFilter(lookup_expr='iexact')
    board = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = NtrcaResult
        fields = ['subject_code','interview_date' , 'board']