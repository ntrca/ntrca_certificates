from django.db import models

class NtrcaResult(models.Model):
    roll = models.PositiveIntegerField(unique=True, null=True)
    # extra info start ---------------------------------
    board = models.IntegerField(blank=True, null=True)
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

    def __str__(self):
        return str(self.name)

