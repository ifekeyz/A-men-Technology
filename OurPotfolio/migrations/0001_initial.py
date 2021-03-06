# Generated by Django 3.1.1 on 2021-08-18 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Image1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('Image2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('Image3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('Category', models.CharField(max_length=50)),
                ('Client', models.CharField(max_length=50)),
                ('Project_date', models.DateField()),
                ('Url', models.CharField(max_length=50)),
                ('Name1', models.CharField(max_length=20)),
                ('Image11', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('Image21', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('Image31', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('Category1', models.CharField(max_length=50)),
                ('Client1', models.CharField(max_length=50)),
                ('Project_date1', models.DateField()),
                ('Url1', models.CharField(max_length=50)),
            ],
        ),
    ]
