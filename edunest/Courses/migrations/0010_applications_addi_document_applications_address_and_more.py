# Generated by Django 4.2.6 on 2023-10-26 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0009_chapter'),
    ]

    operations = [
        migrations.AddField(
            model_name='applications',
            name='addi_document',
            field=models.ImageField(blank=True, null=True, upload_to='courses/images/'),
        ),
        migrations.AddField(
            model_name='applications',
            name='address',
            field=models.TextField(default='addresss'),
        ),
        migrations.AddField(
            model_name='applications',
            name='aply_name',
            field=models.CharField(default='your name', max_length=200),
        ),
        migrations.AddField(
            model_name='applications',
            name='phonenumber',
            field=models.CharField(default='0000000000', max_length=10),
        ),
        migrations.AddField(
            model_name='applications',
            name='pincode',
            field=models.IntegerField(default=0),
        ),
    ]