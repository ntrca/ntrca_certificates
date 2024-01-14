import pandas as pd
import os
import datetime
from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.core.paginator import Paginator
from django.contrib import messages

from candidate.models import Candidate
from .models import NTRCACirtificate
from .utilities import District, ExamsName, Thana, PostOffice
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
                        form_obj.save()
                        request.session['duplicate_roll'] = duplicate_roll
                        return redirect('ntrca_duplicate_certificate', pk=exam_name.pk)
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
                permanent_district__name=all_district,
                exam_name=exam_name
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


def update_result(request):
    pass
    # exam_name = ExamsName.objects.get(pk=1)
    # data = pd.read_csv(os.path.join(os.getcwd(), "fixtures/result_16_pass_18560.csv")) # noqa
    # data_to_dict = data.to_dict(orient='records')
    # num = 0
    # for row in data_to_dict:
    #     try:
    #         data = NtrcaResult.objects.get(roll=row['roll'])
    #         print(data, num)
    #     except Exception as e:
    #         interview_date = datetime.datetime.strptime(row['interview_date'], "%m/%d/%Y").strftime("%Y-%m-%d")
    #         dob = datetime.datetime.strptime(row['dob'], "%m/%d/%Y").strftime("%Y-%m-%d")
    #         data = NtrcaResult.objects.create(
    #             roll=row['roll'], exam_name=exam_name, interview_date=interview_date,
    #             board=row['board'], subject_code=row['subject_code'], name=row['name'],
    #             father=row['father'], mother=row['mother'], s_result=row['s_result'],
    #             h_result=row['h_result'], dob=dob, invoice=row['invoice'], s_number=row['s_number'],
    #             v_number=row['v_number'], total_number=row['total_number'],
    #             comment=row['comment']
    #         )
    #         print(data, num)
    #         num += 1
    # return HttpResponse("Done")


def update_data(request):
    exam_name = ExamsName.objects.get(pk=1)
    candidate = Candidate.objects.all()
    ntrac_tesult = NtrcaResult.objects.all()
    ntrca_cir = NTRCACirtificate.objects.all()
    # Candidate Update
    for obj in candidate:
        obj.exam_name = exam_name
        obj.save()
        print(obj)
    # Result Update
    for obj in ntrac_tesult:
        try:
            _candidate = Candidate.objects.get(roll=obj.roll)
        except Exception:
            _candidate = None
        obj.exam_name = exam_name
        obj.candidate = _candidate
        obj.save()
        print(obj)
    # Cirtificate Update
    for obj in ntrca_cir:
        try:
            result = NtrcaResult.objects.get(roll=obj.roll)
        except Exception:
            result = None
        obj.exam_name = exam_name
        obj.result = result
        obj.save()
        print(obj)
    return HttpResponse("Done")


def update_cirtificate_to_candidate(request):
    for obj in Candidate.objects.all():
        print(obj.roll, "*" * 100)
        try:
            cirti = NTRCACirtificate.objects.get(roll=obj.roll)
            district = District.objects.get(pk=cirti.permanent_district.pk)
            thana = Thana.objects.get(pk=cirti.permanent_police_station.pk)
            post_office = PostOffice.objects.get(pk=cirti.permanent_post_office.pk)
            obj.permanent_vill = cirti.permanent_vill
            obj.permanent_district = district
            obj.permanent_police_station = thana
            obj.permanent_post_office = post_office
            obj.written_number = cirti.written_number
            obj.subject_name = cirti.subject_name
            obj.reg = f"162019{cirti.reg}"
            obj.gender = cirti.gender
            obj.institute_type = cirti.institute_type
            obj.post_name = cirti.post_name
            obj.religion = cirti.religion
            obj.nid = cirti.nid
            obj.post_code = cirti.post_code
            obj.save()
        except Exception as e:
            print(e)
            cirti = None
            district = None
            thana = None
            post_office = None
        print(obj)
    return HttpResponse("Done")
