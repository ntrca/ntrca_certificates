from django.db import models
from django.contrib.auth.models import User
from ntrca_app.utilities import ExamsName, District, Thana, PostOffice
from ntrca_result.models import NtrcaResult


class NtrcaResultPdf(models.Model):
    id = models.AutoField(primary_key=True)
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


class NTRCACirtificate(models.Model):
    id = models.AutoField(primary_key=True)
    result = models.ForeignKey(
        NtrcaResult, on_delete=models.CASCADE, null=True, blank=True
    )
    invoice = models.CharField(max_length=200, null=True)
    exam_name = models.ForeignKey(
        ExamsName, on_delete=models.SET_NULL, null=True, blank=True,
    )
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
    nid = models.CharField(max_length=255, null=True, blank=True)
    religion = models.CharField(max_length=50, null=True)
    permanent_vill = models.TextField(max_length=255, null=True)
    written_number = models.CharField(max_length=200, null=True)
    permanent_district = models.ForeignKey(District, on_delete=models.CASCADE,
        null=True, related_name='permanent_district')
    permanent_police_station = models.ForeignKey(Thana, on_delete=models.CASCADE,
        null=True, related_name='permanent_thana')
    post_office_name = models.CharField(max_length=255, null=True, blank=True)
    viva_mark = models.IntegerField(null=True, blank=True)
    ssc_result = models.DecimalField(null=True, decimal_places=2, max_digits=5, blank=True)
    hsc_result = models.DecimalField(null=True, decimal_places=2, max_digits=5, blank=True)

    class Meta:
        ordering = ['roll']

    def __str__(self):
        return str(self.name)

    @property
    def get_duplicate_count(self):
        """ get certificate duplicate count """
        qs = self.duplicate_certificates.all()
        return len(qs)


class DuplicateCertificate(models.Model):
    """ NTRCA Duplicate Certificate Print Information"""
    id = models.AutoField(primary_key=True)
    ntrca_certificate = models.ForeignKey(
        NTRCACirtificate, on_delete=models.CASCADE,
        related_name='duplicate_certificates'
    )
    note = models.TextField(help_text='Duplicate note', default='General', null=True, blank=True)
    document = models.FileField(null=True, blank=True)
    created_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.ntrca_certificate.name)

class DuplicateCertificateFile(models.Model):
    """ Duplicate certificate files model """
    id = models.AutoField(primary_key=True)
    duplicate_certificate = models.ForeignKey(
        DuplicateCertificate, on_delete=models.CASCADE, null=True,
        related_name='duplicate_certificate_files'
    )
    document = models.FileField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.duplicate_certificate.ntrca_certificate.name)


class PostName(models.Model):
    id = models.AutoField(primary_key=True)
    subject_code = models.IntegerField(blank=True, null=True)
    post_code = models.IntegerField(null=True, blank=True)
    post_name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return str(self.post_name)


class PostAndSubjectCode(models.Model):
    id = models.AutoField(primary_key=True)
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
    id = models.AutoField(primary_key=True)
    roll = models.PositiveIntegerField(null=True)
    subject_code = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "student_valid_data"

    def __str__(self):
        return str(self.roll)

class TotalStudent(models.Model):
    id = models.AutoField(primary_key=True)
    roll = models.PositiveIntegerField(null=True)
    subject_code = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "total_student"
    
    def __str__(self):
        return str(self.roll)

class StudentWrongData(models.Model):
    id = models.AutoField(primary_key=True)
    roll = models.PositiveIntegerField(null=True)
    subject_code = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "student_wrong_data"

    def __str__(self):
        return str(self.roll)
