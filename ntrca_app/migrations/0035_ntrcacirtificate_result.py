# Generated by Django 4.0.6 on 2022-08-02 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ntrca_result', '0003_auto_20220723_1222'),
        ('ntrca_app', '0034_delete_ntrcaresult'),
    ]

    operations = [
        migrations.AddField(
            model_name='ntrcacirtificate',
            name='result',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ntrca_result.ntrcaresult'),
        ),
    ]
