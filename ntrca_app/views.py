from numpy.core.numeric import roll
import pandas as pd
import os
import datetime
from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.core.paginator import Paginator
from django.contrib import messages

from candidate.models import Candidate
from .models import NTRCACirtificate
from .utilities import District, ExamsName
from ntrca_result.models import NtrcaResult
from .forms import DuplicateCertificateForm


def registration(number):
    if number <= 9:
        return f"{'00000' + str(number)}"
    elif number <= 99:
        return f"{'0000' + str(number)}"
    elif number <= 999:
        return f"{'000' + str(number)}"
    elif number <= 9999:
        return f"{'00' + str(number)}"
    elif number <= 99990:
        return f"{'0' + str(number)}"
    else:
        return number

GENDER = (
    (1, 'Male'),
    (2, 'Female'),
    (3, 'Both'),
)


class DashboardView(View):
    template_name = 'dashboard.html'
    def get(self, request):
        exam_name = ExamsName.objects.all()
        context = {
            'exam_name': exam_name,
        }
        return render(request, self.template_name, context)


class NtrcaInputDistrict(View):

    def get(self, request, pk):
        exam_name = ExamsName.objects.get(pk=pk)
        template_name = 'district_input.html'
        all_district = District.objects.all()
        form = DuplicateCertificateForm(request.POST or None)
        context = {
            'all_district': all_district,
            'form': form,
            'object': exam_name
        }
        return render(request, template_name, context)
        
    def post(self, request, pk):
        exam_name = ExamsName.objects.get(pk=pk)
        template_name = 'district_input.html'

        district = request.POST.get('district')
        roll = request.POST.get('roll')
        district_distribution = request.POST.get('district_distribution')
        duplicate_roll = request.POST.get('duplicate_roll')
        if district is not None:
            request.session['all_district'] = district
            return redirect('ntrca_cirtificate_download', pk=exam_name.pk)
        elif roll is not None:
            request.session['single_roll'] = roll
            return redirect('ntrca_single_data', pk=exam_name.pk)
        elif district_distribution is not None:
            request.session['all_data'] = district_distribution
            return redirect('ntrca_district_distribution', pk=exam_name.pk)
        elif duplicate_roll is not None:
            # duplicate_roll section
            try:
                single_data = NTRCACirtificate.objects.get(
                    roll=duplicate_roll, exam_name=exam_name
                )
                if single_data:
                    form = DuplicateCertificateForm(request.POST or None)
                    if form.is_valid():
                        form_obj = form.save(commit=False)
                        form_obj.ntrca_certificate = single_data
                        # form_obj.created_user = request.user  # if have login sys
                        form_obj.save()
                        request.session['duplicate_roll'] = duplicate_roll
                        return redirect('ntrca_duplicate_certificate')
                    else:
                        messages.warning(request, 'Please fill up all required field.')
                        return redirect('ntrca_district', pk=exam_name.pk)
            except Exception as e:
                messages.warning(request, f'Certificate did not found for roll {duplicate_roll}')
                return redirect('ntrca_district', pk=exam_name.pk)
        else:
            message = "Data Not Match"
            return render(request, template_name, {'message': message})


class NtrcaDistrictDistribution(View):
    def get(self, request, pk):
        exam_name = ExamsName.objects.get(pk=pk)
        template_name = 'district_distribution.html'
        all_data = request.session.get('all_data')
        all_datas = NTRCACirtificate.objects.filter(
            permanent_district__name=all_data, exam_name=exam_name
        )
        subject_list = []
        for data in all_datas:
            if data.subject_code not in subject_list:
                subject_list.append(data.subject_code)
        dirsrict_data_list = []
        for data in subject_list:
            obj = NTRCACirtificate.objects.filter(
                subject_code=data,
                permanent_district__name=all_data
            )
            dirsrict_data_list.append(obj)
        context = {
            'thana_wise_data': dirsrict_data_list,
            'district': all_data
        }
        return render(request, template_name, context)


class NtrcaSingleData(View):
    def get(self, request, pk):
        template_name = 'single_data.html'
        exam_name = ExamsName.objects.get(pk=pk)
        single_roll = request.session.get('single_roll')
        single_data = NTRCACirtificate.objects.none()
        try:
            single_data = NTRCACirtificate.objects.get(
                roll=single_roll, exam_name=exam_name
            )
        except Exception as e:
            print(e)
            messages.warning(request, f'Certificate did not found for roll {single_roll}')
            return redirect('ntrca_district', pk=exam_name.pk)

        context = {
            'data': single_data
        }
        return render(request, template_name, context)


class NTRCACirtificateDownloadView(View):
    def get(self, request, pk):
        exam_name = ExamsName.objects.get(pk=pk)
        template_name = 'certificate.html'
        all_district = request.session.get('all_district')
        page_obj = None
        if all_district:
            qs = NTRCACirtificate.objects.filter(
                permanent_district__name=all_district, exam_name=exam_name
            )
            paginator = Paginator(qs, 100)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
        context = {
            'all_data': page_obj
        }
        return render(request, template_name, context)


class NTRCADuplicateCertificatePrintView(View):

    def get(self, request, pk):
        template_name = 'duplicate_certificate.html'
        exam_name = ExamsName.objects.get(pk=pk)
        single_roll = request.session.get('duplicate_roll')
        
        single_data = NTRCACirtificate.objects.none()

        try:
            single_data = NTRCACirtificate.objects.get(
                roll=single_roll, exam_name=exam_name.pk
            )
        except Exception as e:
            messages.warning(request, f'Certificate did not found for roll {single_roll}')
            return redirect('ntrca_district', pk=exam_name.pk)
        context = {
            'data': single_data
        }
        return render(request, template_name, context)


def update_data(request):
    exam_name = ExamsName.objects.get(pk=1)
    ntrac_tesult = NtrcaResult.objects.all()
    ntrca_cir = NTRCACirtificate.objects.all()
    candidate = Candidate.objects.all()
    for obj in ntrca_cir:
        obj.exam_name = exam_name
        obj.save()
        print(obj)
    for obj in ntrac_tesult:
        obj.exam_name = exam_name
        obj.save()
        print(obj)
    for obj in candidate:
        obj.exam_name = exam_name
        obj.save()
        print(obj)
    return HttpResponse("Done")
