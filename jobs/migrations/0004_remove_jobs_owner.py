# Generated by Django 4.1.3 on 2022-12-20 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_alter_jobs_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs',
            name='owner',
        ),
    ]