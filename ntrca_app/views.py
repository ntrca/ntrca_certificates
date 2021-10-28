import pandas as pd
import shutil
from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.core.paginator import Paginator

from .models import (
    NTRCACirtificate, PostAndSubjectCode, StudentValidData, StudentWrongData, Subject,
    TotalStudent
)
from .filters import CandidateFilter
# from .pdf import render_pdf

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
        all_district = NTRCACirtificate.objects.filter(permanent_dist=district)
        district_qs = NTRCACirtificate.objects.filter(
            permanent_dist=district_distribution
        )
        try:
            single_roll = NTRCACirtificate.objects.get(roll=roll)
        except Exception as e:
            print(e)
            single_roll = None
        if all_district.last():
            request.session['all_district'] = [
                district.permanent_dist for district in all_district
            ]
            return redirect('ntrca_cirtificate_download')
        elif single_roll is not None:
            request.session['single_roll'] = single_roll.roll
            return redirect('ntrca_single_data')
        elif district_qs.last():
            request.session['all_data'] = [
                district.permanent_dist for district in district_qs
            ]
            return redirect('ntrca_district_distribution')
        else:
            message = "Data Not Match"
            return render(request, template_name, {'message': message})


class NtrcaDistrictDistribution(View):
    def get(self, request):
        template_name = 'district_distribution.html'
        all_data = request.session.get('all_data')[:1]
        all_datas = NTRCACirtificate.objects.filter(permanent_dist=all_data[0])
        subject_list = []
        for data in all_datas:
            if data.subject_code not in subject_list:
                subject_list.append(data.subject_code)
        subject_list = sorted(subject_list)
        subject_wise_data = []
        for subject in subject_list:
            sub = NTRCACirtificate.objects.filter(
                subject_code=subject,permanent_dist=all_data[0]
            )
            subject_wise_data.append(sub)
        context = {
            'subject_wise_data': subject_wise_data,
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
        all_district = request.session.get('all_district')[:1]
        if all_district:
            qs = NTRCACirtificate.objects.filter(permanent_dist=all_district[0])
            paginator = Paginator(qs, 100)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
        context = {
            'all_data': page_obj
        }
        return render(request, template_name, context)



class NTRCACirtificateView(View):
    def get(self, request):
        template_name = 'certificate.html'
        # read_exl = pd.read_csv("E:/Official/test/ntrca_app/excel/result.csv")
        # excel_list = read_exl.values.tolist()
        # print(excel_list)
        total = 0
        dup = 0
        valid_data = 0

        totaldtat = TotalStudent.objects.all()


        for data in totaldtat:
            try:
                student = NTRCACirtificate.objects.get(roll=data.roll)
                student.written_number = data.score
                student.save()

                StudentValidData.objects.create(
                    roll=data.roll,
                    subject_code=data.subject_code,
                    score=data.score,
                )
                valid_data += 1
            except Exception as e:
                print(e)
                StudentWrongData.objects.create(
                    roll=data.roll,
                    subject_code=data.subject_code,
                    score=data.score,
                )
                dup += 1
        #         StudentValidData.objects.get(roll=data[0])
        #         StudentWrongData.objects.create(
        #             roll=data[0],
        #             subject_code=data[1],
        #             score=data[2],
        #         )
        #         print(f"Duplicate Data")
        #         dup += 1
        #     except Exception as e:
        #         print(e)
        #         TotalStudent.objects.create(
        #             roll=data[0],
        #             subject_code=data[1],
        #             score=data[2],
        #         )
        #         valid_data += 1

            # user = NTRCACirtificate.objects.get(roll=data[0])
            # print(f"Post Code{data[2]} subject code {data[3]}")
            # post = PostAndSubjectCode.objects.get(post_code=data[2], subject_code=data[3])
            # user.post_name = post.post_name
            # user.post_code = post.post_code
            # user.institute_type = post.institute_type
            # user.save()

            total += 1
            print(f"Total Number {total} Valid Data {valid_data} Invalid Data {dup}")
        return HttpResponse("Success")


class ImageMoveOtherFolder(View):
    def get(self, request):
        ntrca_certificate = NTRCACirtificate.objects.all()
        for data in ntrca_certificate:
            source = f"E:/Official/test/ntrca_app/static/photo/{data.invoice}.jpg"
            dastination = f"E:/Official/test/ntrca_app/media/{data.invoice}.jpg"
            shutil.move(source, dastination)
            print(data.invoice)
        return HttpResponse("Success")

