# Generated by Django 3.1.4 on 2022-07-04 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NtrcaResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.PositiveIntegerField(null=True, unique=True)),
                ('board', models.IntegerField(blank=True, null=True)),
                ('interview_date', models.DateField(blank=True, null=True)),
                ('subject_code', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('father', models.CharField(blank=True, max_length=200, null=True)),
                ('mother', models.CharField(blank=True, max_length=200, null=True)),
                ('s_exam', models.CharField(blank=True, max_length=20, null=True)),
                ('s_result', models.CharField(blank=True, max_length=20, null=True)),
                ('s_result_text', models.CharField(blank=True, max_length=20, null=True)),
                ('h_exam', models.CharField(blank=True, max_length=20, null=True)),
                ('h_result', models.CharField(blank=True, max_length=20, null=True)),
                ('h_result_text', models.CharField(blank=True, max_length=20, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('invoice', models.CharField(blank=True, max_length=20, null=True)),
                ('s_number', models.IntegerField(null=True)),
                ('v_number', models.IntegerField(null=True)),
                ('total_number', models.CharField(blank=True, max_length=20, null=True)),
                ('comment', models.CharField(blank=True, default='', max_length=250, null=True)),
            ],
        ),
    ]
