# Generated by Django 3.1.4 on 2021-10-21 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ntrca_app', '0005_ntrcacirtificate'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ntrcacirtificate',
            options={'ordering': ['roll']},
        ),
    ]
