# Generated by Django 4.2.6 on 2023-11-02 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comments', '0003_alter_comment_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]