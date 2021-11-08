from django.db import models
from django.db.models.enums import Choices
from numpy.core.numeric import roll

class NtrcaResult(models.Model):
    roll = models.PositiveIntegerField(null=True)
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


class Subject(models.Model):
    code = models.IntegerField(null=True)
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.name)


class NtrcaResultPdf(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    roll = models.PositiveIntegerField(null=True)
    subject_code = models.IntegerField(blank=True, null=True)
    subject_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = ['subject_code']

    def __str__(self):
        return str(self.name)

GENDER = (
    (1, 'Male'),
    (2, 'Female'),
    (3, 'Both'),
)


class District(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.name)

class Thana(models.Model):
    name = models.CharField(max_length=200, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.name)


class PostOffice(models.Model):
    name = models.CharField(max_length=200, null=True)
    thana = models.ForeignKey(Thana, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.name)


class Village(models.Model):
    name = models.CharField(max_length=200, null=True)
    post_office = models.ForeignKey(PostOffice, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.name)


class NTRCACirtificate(models.Model):
    invoice = models.CharField(max_length=200, null=True)
    roll = models.PositiveIntegerField(null=True)
    reg = models.CharField(null=True, max_length=50)
    name = models.CharField(max_length=200, blank=True, null=True)
    father_name = models.CharField(max_length=200, blank=True, null=True)
    mother_name = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='certificates/', blank=True, null=True)
    subject_code = models.IntegerField(blank=True, null=True)
    subject_name = models.CharField(max_length=200, blank=True, null=True)
    total_number = models.IntegerField(null=True, blank=True)
    post_code = models.IntegerField(null=True, blank=True)
    post_name = models.CharField(max_length=250, null=True)
    institute_type = models.CharField(max_length=255, null=True)
    dob = models.DateTimeField(null=True)
    gender = models.PositiveIntegerField(choices=GENDER, null=True)
    nid = models.CharField(null=True, max_length=255)
    religion = models.CharField(max_length=50, null=True)
    permanent_vill = models.TextField(max_length=255, null=True)
    written_number = models.CharField(max_length=200, null=True)
    permanent_district = models.ForeignKey(District, on_delete=models.CASCADE,
        null=True, related_name='permanent_district')
    permanent_police_station = models.ForeignKey(Thana, on_delete=models.CASCADE,
        null=True, related_name='permanent_thana')
    permanent_post_office = models.ForeignKey(PostOffice, on_delete=models.CASCADE,
        null=True, related_name='permanent_post')
    viva_mark = models.IntegerField(null=True)
    ssc_result = models.DecimalField(null=True, decimal_places=2, max_digits=5)
    hsc_result = models.DecimalField(null=True, decimal_places=2, max_digits=5)

    class Meta:
        ordering = ['roll']

    def __str__(self):
        return str(self.name)


class PostName(models.Model):
    subject_code = models.IntegerField(blank=True, null=True)
    post_code = models.IntegerField(null=True, blank=True)
    post_name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return str(self.post_name)


class PostAndSubjectCode(models.Model):
    subject_name = models.CharField(max_length=255)
    subject_code = models.IntegerField()
    post_code = models.IntegerField()
    post_name = models.CharField(max_length=255)
    institute_type = models.CharField(max_length=255)

    class Meta:
        db_table = "post_sub_name"

    def __str__(self):
        return str(self.subject_name)


class StudentValidData(models.Model):
    roll = models.PositiveIntegerField(null=True)
    subject_code = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "student_valid_data"

    def __str__(self):
        return str(self.roll)

class TotalStudent(models.Model):
    roll = models.PositiveIntegerField(null=True)
    subject_code = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "total_student"
    
    def __str__(self):
        return str(self.roll)

class StudentWrongData(models.Model):
    roll = models.PositiveIntegerField(null=True)
    subject_code = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "student_wrong_data"

    def __str__(self):
        return str(self.roll)
