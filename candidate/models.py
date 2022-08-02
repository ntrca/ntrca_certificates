from django.db import models

from ntrca_app.utilities import ExamsName, District, Thana, PostOffice


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


class Candidate(models.Model):
    id = models.AutoField(primary_key=True)
    invoice = models.CharField(max_length=20, blank=True, null=True)
    exam_name = models.ForeignKey(
        ExamsName, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="candidate_exam_name"
    )
    board = models.IntegerField(blank=True, null=True)
    interview_date = models.DateField(blank=True, null=True)
    roll = models.IntegerField(blank=True, null=True)
    reg = models.CharField(null=True, max_length=50)
    subject_code = models.IntegerField(blank=True, null=True)
    subject_name = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    father = models.CharField(max_length=200, blank=True, null=True)
    mother = models.CharField(max_length=200, blank=True, null=True)
    gender = models.PositiveIntegerField(choices=GENDER, null=True)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    s_exam = models.CharField(max_length=200, blank=True, null=True)
    s_result = models.CharField(max_length=200, blank=True, null=True)
    s_result_text = models.CharField(max_length=200, blank=True, null=True)
    h_exam = models.CharField(max_length=200, blank=True, null=True)
    h_result = models.CharField(max_length=200, blank=True, null=True)
    h_result_text = models.CharField(max_length=200, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    written_number = models.CharField(max_length=200, null=True)
    post_code = models.IntegerField(null=True, blank=True)
    post_name = models.CharField(max_length=250, null=True)
    institute_type = models.CharField(max_length=255, null=True)
    nid = models.CharField(max_length=255, null=True, blank=True)
    religion = models.CharField(max_length=50, null=True)
    permanent_vill = models.TextField(max_length=255, null=True)
    permanent_district = models.ForeignKey(District, on_delete=models.CASCADE,
        null=True, related_name='district')
    permanent_police_station = models.ForeignKey(Thana, on_delete=models.CASCADE,
        null=True, related_name='thana')
    permanent_post_office = models.ForeignKey(PostOffice, on_delete=models.CASCADE,
        null=True, related_name='post')

    # def save(self, *args, **kwargs):
    #     if not self.reg and self.exam_name.year and self.exam_name.examth:
    #         number = Candidate.objects.all().count()
    #         reg_no = registration(number)
    #         self.reg = f"{self.exam_name.examth}{self.exam_name.year}{reg_no}"
    #     return super().save(*args, **kwargs)

    class Meta:
        ordering = ['roll']

    def __str__(self):
        return self.invoice
    