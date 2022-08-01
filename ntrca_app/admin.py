from django.contrib import admin
from .models import (
    NtrcaResultPdf, Subject, PostName,
    NTRCACirtificate, PostAndSubjectCode, District, Thana, PostOffice,
    DuplicateCertificate, DuplicateCertificateFile, ExamsName
)


class NtrcaResultPdfAdmin(admin.ModelAdmin):
    list_display = [
    'roll','name',
    ]
    list_filter = ['subject_name']
admin.site.register(NtrcaResultPdf, NtrcaResultPdfAdmin)


class SubjectAdmin(admin.ModelAdmin):
    list_display = [
    'code','name',
    ]

admin.site.register(Subject, SubjectAdmin)


class ExamsNameAdmin(admin.ModelAdmin):
    list_display = [
    'code','name',
    ]
admin.site.register(ExamsName, ExamsNameAdmin)

class DuplicateCertificateInline(admin.TabularInline):
    model = DuplicateCertificate
    extra = 0
    readonly_fields = ['created', 'updated']

class NTRCACirtificateAdmin(admin.ModelAdmin):
    list_display = [
    'invoice','name', 'roll', 'reg', 'subject_code', 'post_code', 'subject_name',
    'total_number',
    ]
    list_filter = ['subject_code']
    search_fields = ['roll', 'name', 'invoice']
    inlines = [
        DuplicateCertificateInline,
    ]


admin.site.register(NTRCACirtificate, NTRCACirtificateAdmin)

class PostNameAdmin(admin.ModelAdmin):
    list_display = [
    'subject_code', 'post_code', 'post_name',
    ]
    list_filter = ['subject_code']
admin.site.register(PostName, PostNameAdmin)


class PostAndSubjectCodeAdmin(admin.ModelAdmin):
    list_display = [
    'subject_code', 'post_code', 'post_name', 'institute_type'
    ]
    list_filter = ['subject_code']
admin.site.register(PostAndSubjectCode, PostAndSubjectCodeAdmin)


class DistrictAdmin(admin.ModelAdmin):
    list_display = [
    'name'
    ]
admin.site.register(District, DistrictAdmin)


class ThanaAdmin(admin.ModelAdmin):
    list_display = [
    'name', 'district'
    ]
admin.site.register(Thana, ThanaAdmin)


class PostOfficeAdmin(admin.ModelAdmin):
    list_display = [
    'name', 'thana'
    ]
    search_fields = ['name', 'thana__name']
admin.site.register(PostOffice, PostOfficeAdmin)
