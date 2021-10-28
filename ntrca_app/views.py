from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.core.paginator import Paginator

from .models import NTRCACirtificate


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
        return render(request, template_name)
    def post(self, request):
        template_name = 'district_input.html'

        district = request.POST.get('district')
        roll = request.POST.get('roll')
        district_distribution = request.POST.get('district_distribution')

        if district:
            request.session['all_district'] = district
            return redirect('ntrca_cirtificate_download')
        elif roll:
            request.session['single_roll'] = roll
            return redirect('ntrca_single_data')
        elif district_distribution:
            request.session['all_data'] = district_distribution
            return redirect('ntrca_district_distribution')
        else:
            message = "Data Not Match"
            return render(request, template_name, {'message': message})


class NtrcaDistrictDistribution(View):
    def get(self, request):
        template_name = 'district_distribution.html'
        all_data = request.session.get('all_data')
        all_datas = NTRCACirtificate.objects.filter(permanent_dist=all_data)
        subject_list = []
        for data in all_datas:
            if data.subject_code not in subject_list:
                subject_list.append(data.subject_code)
        subject_list = sorted(subject_list)
        subject_wise_data = []
        for subject in subject_list:
            sub = NTRCACirtificate.objects.filter(
                subject_code=subject,permanent_dist=all_data
            )
            subject_wise_data.append(sub)
        context = {
            'subject_wise_data': subject_wise_data,
            'district': all_data,
        }
        return render(request, template_name, context)


class NtrcaSingleData(View):
    def get(self, request):
        template_name = 'single_data.html'
        single_roll = request.session.get('single_roll')
        try:
            single_data = NTRCACirtificate.objects.get(roll=single_roll)
        except Exception as e:
            print(e)
            message = "Roll Not Found"
        context = {
            'data': single_data
        }
        return render(request, template_name, context)


class NTRCACirtificateDownloadView(View):
    def get(self, request):
        template_name = 'certificate.html'
        all_district = request.session.get('all_district')
        if all_district:
            qs = NTRCACirtificate.objects.filter(permanent_dist=all_district)
            paginator = Paginator(qs, 100)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
        context = {
            'all_data': page_obj
        }
        return render(request, template_name, context)


class NTRCACirtificateView(View):
    def get(self, request):
        return HttpResponse("Success")
