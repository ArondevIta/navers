# Generated by Django 3.1 on 2020-08-16 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20200815_2328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='navers',
        ),
    ]