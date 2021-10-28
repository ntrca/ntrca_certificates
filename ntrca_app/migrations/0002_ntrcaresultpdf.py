# Generated by Django 3.1.4 on 2021-10-18 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ntrca_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NtrcaResultPdf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('roll', models.PositiveIntegerField(null=True)),
                ('subject_code', models.IntegerField(blank=True, null=True)),
                ('subject_name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
