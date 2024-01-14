import os
from django.shortcuts import HttpResponse
from django.views import View
from ntrca_app.models import District, Thana

import pandas as pd


class UpdateDistrict(View):
    def get(self, request):
        data = pd.read_csv(os.path.join(os.getcwd(), "DB/CSV/div_dist_thana.csv")) # noqa
        data_to_dict = data.to_dict(orient='records')
        print(data_to_dict)
        for row in data_to_dict:
            pass
        return HttpResponse(f"Data")


class UpdateResult(View):
    def get(self, request):
        data = pd.read_excel(os.path.join(os.getcwd(), "DB/excel/final_pass_list.xlsx")) # noqa
        data_to_dict = data.to_dict(orient='records')
        print(data_to_dict)
        for row in data_to_dict:
            pass
        return HttpResponse(f"Data")
