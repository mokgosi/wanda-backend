# Generated by Django 3.2.8 on 2021-11-06 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20211106_0916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='name',
        ),
    ]
