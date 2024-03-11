# Generated by Django 4.2.6 on 2023-11-16 05:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Testseries', '0003_quizresponse_is_bookmarked'),
    ]

    operations = [
        migrations.AddField(
            model_name='testseries',
            name='faculty',
            field=models.ForeignKey(default=40, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testseries',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]
