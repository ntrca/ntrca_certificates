# Generated by Django 3.1.4 on 2020-12-02 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0002_auto_20201202_1557'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='candidate',
            options={'ordering': ['roll']},
        ),
    ]
