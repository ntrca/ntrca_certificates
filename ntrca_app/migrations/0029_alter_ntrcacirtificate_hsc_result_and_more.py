# Generated by Django 4.2.9 on 2024-01-15 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ntrca_app', '0028_ntrcacirtificate_result_postoffice_code_thana_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ntrcacirtificate',
            name='hsc_result',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ntrcacirtificate',
            name='ssc_result',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
