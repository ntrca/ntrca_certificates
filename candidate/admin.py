from django.contrib import admin
from import_export.admin import (
    ImportExportModelAdmin, ImportExportActionModelAdmin
)

from .models import Candidate

class CandidateAdmin(ImportExportActionModelAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 'board', 'subject_code', 'roll', 'interview_date', 'name', 'father', 'mother', 'dob', 'invoice']
    list_filter = ['board', 'interview_date', 'subject_code']
    search_fields = ['roll']

admin.site.register(Candidate, CandidateAdmin)