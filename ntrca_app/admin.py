from django.contrib import admin
from .models import (
    NtrcaResult, NtrcaResultPdf, Subject, PostName,
    NTRCACirtificate, PostAndSubjectCode, District, Thana, PostOffice,
    DuplicateCertificate, DuplicateCertificateFile
)

class NtrcaMoelAdmin(admin.ModelAdmin):
    list_display = [
        'pk','roll','s_number', 'v_number',
        'total_number','name','father','comment', 'interview_date'
    ]

admin.site.register(NtrcaResult, NtrcaMoelAdmin)


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

class DuplicateCertificateInline(admin.TabularInline):
    model = DuplicateCertificate
    extra = 0

class NTRCACirtificateAdmin(admin.ModelAdmin):
    list_display = [
    'invoice','name', 'roll', 'reg', 'subject_code', 'post_code', 'subject_name',
    'total_number',
    ]
    list_filter = ['subject_code']
    search_fields = ['roll', 'name']
    inlines = [
        DuplicateCertificateInline,
    ]


admin.site.register(NTRCACirtificate, NTRCACirtificateAdmin)

@admin.register(DuplicateCertificate)
class DuplicateCertificateAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'ntrca_certificate',
        'note',
        'document',
        'created_user',
        'created',
        'updated',
    )
    list_filter = ('ntrca_certificate', 'created_user', 'created', 'updated')
    search_fields = ['ntrca_certificate__name',]


# @admin.register(DuplicateCertificateFile)
# class DuplicateCertificateFileAdmin(admin.ModelAdmin):
#     list_display = (
#         'id',
#         'duplicate_certificate',
#         'document',
#         'created',
#         'updated',
#     )
#     list_filter = ('duplicate_certificate', 'created', 'updated')

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
