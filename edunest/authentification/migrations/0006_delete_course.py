# Generated by Django 4.2.6 on 2023-10-19 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0005_alter_course_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Course',
        ),
    ]