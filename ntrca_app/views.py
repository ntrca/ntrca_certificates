from numpy.core.numeric import roll
import pandas as pd
from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import HttpResponseRedirect

from .models import NTRCACirtificate, District, Thana, PostOffice
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


class NtrcaInputDistrict(View):

    def get(self, request):
        template_name = 'district_input.html'
        all_district = District.objects.all()
        form = DuplicateCertificateForm(request.POST or None)
        context = {
            'all_district': all_district,
            'form': form
        }
        return render(request, template_name, context)
        
    def post(self, request):
        template_name = 'district_input.html'

        district = request.POST.get('district')
        roll = request.POST.get('roll')
        district_distribution = request.POST.get('district_distribution')
        duplicate_roll = request.POST.get('duplicate_roll')
        print('input data', district, roll, district_distribution, duplicate_roll)
      
        if district is not None:
            request.session['all_district'] = district
            return redirect('ntrca_cirtificate_download')
        elif roll is not None:
            request.session['single_roll'] = roll
            return redirect('ntrca_single_data')
        elif district_distribution is not None:
            request.session['all_data'] = district_distribution
            return redirect('ntrca_district_distribution')
        elif duplicate_roll is not None:
            # duplicate_roll section
            try:
                single_data = NTRCACirtificate.objects.get(roll=duplicate_roll)
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
                        return redirect('ntrca_district')
            except Exception as e:
                messages.warning(request, f'Certificate did not found for roll {duplicate_roll}')
                return redirect('ntrca_district')
        else:
            message = "Data Not Match"
            return render(request, template_name, {'message': message})


class NtrcaDistrictDistribution(View):
    def get(self, request):
        template_name = 'district_distribution.html'
        all_data = request.session.get('all_data')
        all_datas = NTRCACirtificate.objects.filter(
            permanent_district__name=all_data
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
    def get(self, request):
        template_name = 'single_data.html'
        single_roll = request.session.get('single_roll')
        
        single_data = NTRCACirtificate.objects.none()

        try:
            single_data = NTRCACirtificate.objects.get(roll=single_roll)
        except Exception as e:
            print(e)
            message = "Roll Not Found"
            messages.warning(request, f'Certificate did not found for roll {single_roll}')
            return HttpResponseRedirect('/')

        context = {
            'data': single_data
        }
        return render(request, template_name, context)


class NTRCACirtificateDownloadView(View):
    def get(self, request):
        template_name = 'certificate.html'
        all_district = request.session.get('all_district')
        page_obj = None
        if all_district:
            qs = NTRCACirtificate.objects.filter(permanent_district__name=all_district)
            paginator = Paginator(qs, 100)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
        context = {
            'all_data': page_obj
        }
        return render(request, template_name, context)


class NTRCACirtificateView(View):
    def get(self, request):
        reat_data = pd.read_excel("E:/Official/ntrca_certificates/ntrca_app/excel/education.xlsx")
        list_data = reat_data.values.tolist()
        print(list_data)
        count = 1
        for data in list_data:
            obj = NTRCACirtificate.objects.get(roll=data[0])
            try:
                data1 = float(data[1])
                data2 = float(data[2])
            except Exception as e:
                print(e, "*" * 100)
                data1 = data[1]
                data2 = data[2]
            print(type(data1), "#" * 100, type(data2), "@" * 100)
            if type(data1) == int or type(data1) == float:
                if data1 <= 5.00 and data1 >= 2.00:
                    print(f"SSC Data Varified")
                    obj.ssc_result = data1
                else:
                    obj.ssc_result = None
                obj.save()
            if type(data2) == int or type(data2) == float:
                if data2 <= 5 and data2 >= 2:
                    print(f"HSC Data Varified")
                    obj.hsc_result = data2
                    obj.save()
                else:
                    obj.hsc_result = None
                obj.save()
            print(f"Roll {obj.roll} SSC Result {obj.ssc_result} {data[1]} Hsc Result {obj.hsc_result} {data[2]} Loop {count}")
            count += 1
        return HttpResponse("Success")


class NTRCADuplicateCertificatePrintView(View):

    def get(self, request):
        template_name = 'duplicate_certificate.html'
        single_roll = request.session.get('duplicate_roll')
        
        single_data = NTRCACirtificate.objects.none()

        try:
            single_data = NTRCACirtificate.objects.get(roll=single_roll)
        except Exception as e:
            messages.warning(request, f'Certificate did not found for roll {single_roll}')
            return HttpResponseRedirect('/')

        context = {
            'data': single_data
        }
        return render(request, template_name, context)