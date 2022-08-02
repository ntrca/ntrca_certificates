import os
import pandas as pd
from django.db import connections
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse

from ntrca_app.utilities import ExamsName
from .models import Candidate

def get_data():
    try:
        with connections['result'].cursor() as cursor:
            get_data = """
                select board, interview_date, roll,
                subject_code,
                name,
                father,
                mother,
                s_exam,
                s_result,
                s_result_text,
                h_exam,
                h_result,
                h_result_text,
                dob,
                invoice from candidate_data
            """
            try:
                cursor.execute(get_data)
            except Exception as e:
                print(e)
            validate_data = cursor.fetchall()
            print(validate_data)
            roll = validate_data[0][2]
            print(roll)
    except Exception as e:
        print(e)
    return validate_data

def create_data(request):
    validate_data = get_data()
    count = 1
    for data in validate_data:
        try:
            cinfo = Candidate.objects.get(invoice=data[14])
            print('EXISTS DATA*********')
        except:
            Candidate.objects.create(
                board=data[0],
                interview_date=data[1],
                roll=data[2],
                subject_code=data[3],
                name=data[4],
                father=data[5],
                mother=data[6],
                s_exam=data[7],
                s_result=data[8],
                s_result_text=data[9],
                h_exam=data[10],
                h_result=data[11],
                h_result_text=data[12],
                dob=data[13],
                invoice=data[14]
            )
            print(f"CREATED: {count}")
            count += 1


class ImportCandidate(View):
    def get(self, request):
        data = pd.read_json(os.path.join(os.getcwd(), "DB/json/Candidate-2022-07-05.json"))
        data_to_dict = data.to_dict(orient='records')
        total = 0
        get_data = 0
        create_data = 0
        for row in data_to_dict:
            try:
                get_candidate = Candidate.objects.get(roll=row['roll'])
                get_data += 1
                print(f" Get Data {get_candidate}, {get_data}")
            except Exception as e:
                Candidate.objects.create(
                    id=row['id'], board=row['board'], interview_date=row['interview_date'],
                    roll=row['roll'], subject_code=row['subject_code'], name=row['name'],
                    father=row['father'], mother=row['mother'], s_exam=row['s_exam'],
                    s_result=row['s_result'], s_result_text=row['s_result_text'],
                    h_exam=row['h_exam'], h_result=row['h_result'], invoice=row['invoice'],
                    h_result_text=row['h_result_text'], dob=row['dob'],
                    exam_name=ExamsName.objects.get(pk=1)
                )
                create_data += 1
                print(create_data, "*" * 100)
            total += 0
        return HttpResponse(f"Data {get_data} + {create_data} = {total}")
