# Generated by Django 4.1.3 on 2022-12-11 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=240, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=240, verbose_name='last Name')),
                ('phone', models.CharField(max_length=240, verbose_name='Phone')),
                ('email', models.EmailField(max_length=254)),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
