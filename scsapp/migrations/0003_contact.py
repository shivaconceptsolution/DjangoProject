# Generated by Django 2.2.7 on 2019-12-18 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scsapp', '0002_register_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailid', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=12)),
                ('message', models.CharField(max_length=200)),
            ],
        ),
    ]
