# Generated by Django 3.2.7 on 2021-10-07 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OurPotfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]