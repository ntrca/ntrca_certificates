# Generated by Django 3.1.4 on 2021-10-19 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ntrca_app', '0003_subject'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ntrcaresultpdf',
            options={'ordering': ['subject_code']},
        ),
    ]
