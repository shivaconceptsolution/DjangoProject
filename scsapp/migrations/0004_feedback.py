# Generated by Django 2.2.7 on 2019-12-26 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scsapp', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailid', models.CharField(max_length=200)),
                ('feeddesc', models.CharField(max_length=200)),
                ('feedto', models.CharField(max_length=200)),
            ],
        ),
    ]
