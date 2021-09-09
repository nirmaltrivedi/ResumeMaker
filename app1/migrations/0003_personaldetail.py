# Generated by Django 3.2.6 on 2021-09-08 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_rename_contact_detail_contactdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(default='', max_length=20)),
                ('midname', models.CharField(default='', max_length=20)),
                ('lastname', models.CharField(default='', max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('contact_no', models.PositiveIntegerField()),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
