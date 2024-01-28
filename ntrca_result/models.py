from django.db import models
from ntrca_app.utilities import ExamsName
from candidate.models import Candidate

class NtrcaResult(models.Model):
    id = models.AutoField(primary_key=True)
    candidate = models.ForeignKey(
        Candidate, on_delete=models.CASCADE, null=True, blank=True
    )
    roll = models.PositiveIntegerField(unique=True, null=True)
    exam_name = models.ForeignKey(
        ExamsName, on_delete=models.SET_NULL, null=True, blank=True,
    )
    # extra info start ---------------------------------
    board = models.CharField(max_length=200, blank=True, null=True)
    interview_date = models.DateField(blank=True, null=True)
    subject_code = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    father = models.CharField(max_length=200, blank=True, null=True)
    mother = models.CharField(max_length=200, blank=True, null=True)
    s_exam = models.CharField(max_length=20, blank=True, null=True)
    s_result = models.CharField(max_length=20, blank=True, null=True)
    s_result_text = models.CharField(max_length=20, blank=True, null=True)
    h_exam = models.CharField(max_length=20, blank=True, null=True)
    h_result = models.CharField(max_length=20, blank=True, null=True)
    h_result_text = models.CharField(max_length=20, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    invoice = models.CharField(max_length=20, blank=True, null=True)
    # extra info end --------------------------------------
    s_number = models.IntegerField(null=True)
    v_number = models.IntegerField(null=True)
    total_number = models.CharField(max_length=20, null=True, blank=True)
    comment = models.CharField(max_length=250, blank=True, null=True, default="")

    def save(self, *args, **kwargs):
        if self.s_number or self.v_number:
            self.total_number = self.s_number + self.v_number
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.candidate} {self.id}"

