# Generated by Django 4.2.9 on 2024-01-14 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ntrca_app', '0041_ntrcacirtificate_permanent_vill'),
    ]

    operations = [
        migrations.AddField(
            model_name='ntrcacirtificate',
            name='certificate_marks',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]