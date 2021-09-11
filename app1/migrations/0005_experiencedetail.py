# Generated by Django 3.2.6 on 2021-09-11 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20210911_1007'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExperienceDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=500)),
                ('company', models.CharField(max_length=500)),
                ('job_started', models.DateField()),
                ('job_completed', models.DateField()),
                ('responsibilities', models.CharField(blank=True, max_length=5000)),
                ('achievements', models.CharField(blank=True, max_length=2000)),
            ],
        ),
    ]