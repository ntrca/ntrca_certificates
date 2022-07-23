from ntrca_app.models import NTRCACirtificate, ExamsName
from ntrca_result.models import NtrcaResult


def update_data():
    exam_name = ExamsName.objects.get(pk=1)
    num = 0
    num2 = 0
    for obj in NTRCACirtificate:
        obj.exam_name = exam_name
        num += 1
        print(f"NTRCA Certi: {num}")
        # obj.save()
    for obj in NtrcaResult:
        obj.exam_name = exam_name
        num2 += 1
        print(f"NTRCA Certi: {num2}")
        # obj.save()
