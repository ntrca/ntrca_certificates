# Generated by Django 3.1.4 on 2021-10-24 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ntrca_app', '0012_auto_20211024_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ntrcacirtificate',
            name='dob',
            field=models.DateTimeField(null=True),
        ),
    ]
