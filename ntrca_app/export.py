import xlwt

from django.http import HttpResponse
from .models import NtrcaResult

def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="ntrca_result.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Roll','Name','Father Name', 'Mother Name', 'Subject Code', 'SSC Result', 'Certificate Number', 'Viva Number', 'Total Number', 'Comment']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = NtrcaResult.objects.all().values_list('roll','name','father', 'mother', 'subject_code', 's_result', 's_number', 'v_number', 'total_number', 'comment')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response
        