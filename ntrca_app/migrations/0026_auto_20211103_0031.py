# Generated by Django 3.1.4 on 2021-11-02 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ntrca_app', '0025_ntrcacirtificate_viva_mark'),
    ]

    operations = [
        migrations.AddField(
            model_name='ntrcacirtificate',
            name='hsc_result',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='ntrcacirtificate',
            name='ssc_result',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]