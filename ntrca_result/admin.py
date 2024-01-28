from django.contrib import admin
from .models import NtrcaResult

class NtrcaMoelAdmin(admin.ModelAdmin):
    list_display = [
    'pk','roll','s_number', 'v_number', 'total_number','name','father','comment', 'interview_date'
    ]
    search_fields = ['roll']

admin.site.register(NtrcaResult, NtrcaMoelAdmin)