import pandas as pd
import os
import datetime
from ntrca_app.models import ExamsName
from ntrca_result.models import NtrcaResult


def update_data():
    exam_name = ExamsName.objects.get(pk=1)
    data = pd.read_excel(os.path.join(os.getcwd(), "fixtures/result_16_pass_18560.csv")) # noqa
    data_to_dict = data.to_dict(orient='records')
    for row in data_to_dict:
        try:
            data = NtrcaResult.objects.get(roll=row['roll'])
            print(data, num)
        except Exception as e:
            interview_date = datetime.datetime.strptime(row['interview_date'], "%d/%m/%Y").strftime("%Y-%m-%d")
            dob = datetime.datetime.strptime(row['dob'], "%d/%m/%Y").strftime("%Y-%m-%d")
            data = NtrcaResult.objects.create(
                roll=row['roll'], exam_name=exam_name, interview_date=interview_date,
                board=row['board'], subject_code=row['subject_code'], name=row['name'],
                father=row['father'], mother=row['mother'], s_result=row['s_result'],
                h_result=row['h_result'], dob=dob, invoice=row['invoice'], s_number=row['s_number'],
                v_number=row['v_number'], total_number=row['total_number'],
                comment=row['comment']
            )
            print(data, num)
            num += 1
update_data()
