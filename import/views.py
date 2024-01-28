import os
import pandas as pd
from django.shortcuts import HttpResponse, render
from django.views import View
from ntrca_app.models import District, Thana, NTRCACirtificate, ExamsName
from ntrca_app.views import registration


class UpdateDistrict(View):
    def get(self, request):
        data = pd.read_csv(os.path.join(os.getcwd(), "DB/CSV/div_dist_thana.csv")) # noqa
        data_to_dict = data.to_dict(orient='records')
        print(data_to_dict)
        for row in data_to_dict:
            print(row['dist_name'], "********", row['thana'])
            dis = District.objects.get(name=row['dist_name'])
            dis.code = row['dist_code']
            dis.save()

            # Thana
            try:
                thana = Thana.objects.get(district=dis, name=row['thana'])
                thana.code = row['thana_code']
                thana.save()
            except Exception as e:
                print(e)
        return HttpResponse(f"Data")


class UpdateResult(View):
    def get(self, request):
        return render(request, 'upload_excel.html')
    def post(self, request):
        if request.method == 'POST' and request.FILES['excel_file']:
            excel_file = request.FILES['excel_file']
            
            # Check if the file is an Excel file
            if excel_file.name.endswith('.csv'):
                # data = pd.read_csv(os.path.join(os.getcwd(), excel_file)).fillna(0) # noqa
                data = pd.read_csv(excel_file).fillna(0) # noqa
                data_to_dict = data.to_dict(orient='records')
                match = 0
                exam_name = ExamsName.objects.get(code='002')
                for row in data_to_dict:
                    print(f"{row['invoice']}")
                    # try:
                    district = District.objects.get(name=row['district_name'])
                    exam_name = ExamsName.objects.get(code='002')
                    NTRCACirtificate.objects.get_or_create(
                        invoice=row['invoice'], exam_name=exam_name, roll=row['roll'],
                        father_name=row['father_name'], mother_name=row['mother_name'],
                        subject_code=row['subject_code'], subject_name=row['subject_name'],
                        total_number=row['total_number'], post_code=row['post_code'],
                        post_name=row['post_name'], institute_type=row['institute_type'],
                        dob=row['dob'], gender=row['gender'], religion=row['religion'],
                        written_number=row['written_number'], permanent_district=district,
                        police_station_name=row['police_station_name'], post_office_name=row['post_office_name'],
                        permanent_vill=row['permanent_vill'], name=row['name'],
                        viva_mark=row['viva_mark'], ssc_result=row['ssc_result'], hsc_result=row['hsc_result']
                    )
                    # except Exception as e:
                    #     print(e)
                regs = NTRCACirtificate.objects.filter(exam_name=exam_name).order_by('permanent_district__code', 'roll')
                for obj in regs:
                    match += 1
                    print(f"match: {match} Update reg: {obj.permanent_district.name}")
                    obj.reg = f"{registration(match)}"
                    obj.save()

                return HttpResponse(f"Match {match} Total {match}")
            else:
                return render(request, 'upload_excel.html')


def delete_cer(request):
    NTRCACirtificate.objects.filter(exam_name__code='002').delete()
    return HttpResponse("Done")
