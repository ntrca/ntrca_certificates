from django.db import models


class ExamsName(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    code = models.CharField(unique=True, max_length=255)
    year = models.PositiveIntegerField()
    examth = models.CharField(max_length=255)
    reg_prefixed = models.CharField(max_length=255, null=True, blank=True)
    publish_date = models.DateField(null=True, blank=True)
    certificate_pass = models.DecimalField(max_digits=12, default=0.00, decimal_places=2)
    viva_pass = models.DecimalField(max_digits=12, default=0.00, decimal_places=2)

    def __str__(self):
        return self.name


class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.IntegerField(null=True)
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.name)


class District(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.name)


class Thana(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.name)


class PostOffice(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    thana = models.ForeignKey(Thana, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.name)


class Village(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    post_office = models.ForeignKey(PostOffice, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.name)

