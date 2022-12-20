# Generated by Django 4.1.3 on 2022-12-13 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='sales_retail',
            field=models.CharField(choices=[('Sales Representative', 'Sales Representative'), ('Inside Sales', 'Inside Sales'), ('Outside Sales', 'Outside Sales'), ('Technical Sales', 'Technical Sales'), ('Sales Engineers', 'Sales Engineers'), ('Sales Management', 'Sales Management'), ('Retail Sales', 'Retail Sales'), ('Accounting Management', 'Accounting Management'), ('Business Development', 'Business Development'), ('Retail Outlet Management', 'Retail Outlet Management'), ('Supermarket Management', 'Supermarket Management'), ('Department Store Management', 'Department Store Management'), ('Hypermarket Management', 'Hypermarket Management')], default='', max_length=240),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='specialism',
            field=models.CharField(choices=[('Sales & Retail', 'Sales & Retail'), ('Marketing', 'Marketing'), ('Media', 'Media, communication & Writing'), ('Consumer Service', 'Consumer Service'), ('Art', 'Art, Fashion & Design'), ('Entertainment', 'Consumer Service'), ('IT & Programming', 'IT & Programming'), ('Data Science', 'Data Science'), ('Operation', 'Operation & General Management'), ('Manufacturing', 'Manufacturing'), ('Supply Chain', 'Supply Chain, Transport and Logistics'), ('Engineering-Design', 'Engineering- Design, Installations, Operations & Maintanance'), ('Engineering-Construction', 'Engineering, Construction & Planning'), ('Energy & Mining', 'Energy & Mining'), ('Science & Lab', 'Science & Lab Professionals'), ('Finance', 'Finance, Accounting & Auditing'), ('Banking', 'Banking & Investing Management'), ('Office & Admin', 'Office & Admin'), ('Hospitality', 'Restaurant & Hospitality'), ('Security', 'Security'), ('HR & Training', 'HR & Training'), ('Coaching & Motivation', 'Coaching & Motivation'), ('Social Science', 'Social Science, Research and Qualitative Assessors'), ('Agriculture', 'Agriculture, Forestry and Animal Care'), ('Legal', 'Legal'), ('Health Care', 'Health Care and Pharmacy'), ('Education', 'Education'), ('Real Estate', 'Real Estate'), ('Insurance', 'Insurance'), ('Aviation', 'Aviation, Travel & Tourism'), ('Government', 'Government, Government Relations, International Relations & Public Administration'), ('Business Executive', 'Business Executives'), ('Other', 'Other')], default='', max_length=240),
        ),
    ]