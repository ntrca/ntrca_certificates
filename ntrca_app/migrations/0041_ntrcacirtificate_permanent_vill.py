# Generated by Django 4.2.9 on 2024-01-14 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ntrca_app', '0040_remove_ntrcacirtificate_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ntrcacirtificate',
            name='permanent_vill',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
