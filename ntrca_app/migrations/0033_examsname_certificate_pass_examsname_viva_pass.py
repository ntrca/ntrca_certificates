# Generated by Django 4.0.6 on 2022-08-01 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ntrca_app', '0032_auto_20220723_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='examsname',
            name='certificate_pass',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
        migrations.AddField(
            model_name='examsname',
            name='viva_pass',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
    ]