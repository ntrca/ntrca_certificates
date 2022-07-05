from django.db import models

# Create your models here.


class Candidate(models.Model):
    board = models.IntegerField(blank=True, null=True)
    interview_date = models.DateField(blank=True, null=True)
    roll = models.IntegerField(blank=True, null=True)
    subject_code = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    father = models.CharField(max_length=200, blank=True, null=True)
    mother = models.CharField(max_length=200, blank=True, null=True)
    s_exam = models.CharField(max_length=200, blank=True, null=True)
    s_result = models.CharField(max_length=200, blank=True, null=True)
    s_result_text = models.CharField(max_length=200, blank=True, null=True)
    h_exam = models.CharField(max_length=200, blank=True, null=True)
    h_result = models.CharField(max_length=200, blank=True, null=True)
    h_result_text = models.CharField(max_length=200, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    invoice = models.CharField(max_length=20, blank=True, null=True)


    class Meta:
        ordering = ['roll']


    def __str__(self):
        return self.invoice
    