# Generated by Django 3.1.4 on 2022-02-02 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ntrca_app', '0028_duplicatecertificate_duplicatecertificatefile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duplicatecertificate',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
