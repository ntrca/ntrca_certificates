# Generated by Django 3.1.4 on 2021-10-26 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ntrca_app', '0019_postandsubjectcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='ntrcacirtificate',
            name='institute_type',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
