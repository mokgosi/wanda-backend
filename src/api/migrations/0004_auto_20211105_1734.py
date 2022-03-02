# Generated by Django 3.2.8 on 2021-11-05 17:34

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20211105_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='detail',
        ),
        migrations.AddField(
            model_name='page',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AddField(
            model_name='page',
            name='name',
            field=models.CharField(default='page-name', max_length=100),
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(default='page-title', max_length=255),
        ),
    ]
