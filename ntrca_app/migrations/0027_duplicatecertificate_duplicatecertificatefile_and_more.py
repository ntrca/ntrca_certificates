# Generated by Django 4.2.9 on 2024-01-14 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ntrca_app', '0026_auto_20211103_0031'),
    ]

    operations = [
        migrations.CreateModel(
            name='DuplicateCertificate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('note', models.TextField(blank=True, default='General', help_text='Duplicate note', null=True)),
                ('document', models.FileField(blank=True, null=True, upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DuplicateCertificateFile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('document', models.FileField(null=True, upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExamsName',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255, unique=True)),
                ('year', models.PositiveIntegerField()),
                ('examth', models.CharField(max_length=255)),
                ('reg_prefixed', models.CharField(blank=True, max_length=255, null=True)),
                ('publish_date', models.DateField(blank=True, null=True)),
                ('certificate_pass', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('viva_pass', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
            ],
        ),
        migrations.DeleteModel(
            name='NtrcaResult',
        ),
        migrations.RemoveField(
            model_name='ntrcacirtificate',
            name='permanent_post_office',
        ),
        migrations.AddField(
            model_name='district',
            name='code',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ntrcacirtificate',
            name='certificate_marks',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ntrcacirtificate',
            name='police_station_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='ntrcacirtificate',
            name='post_office_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
