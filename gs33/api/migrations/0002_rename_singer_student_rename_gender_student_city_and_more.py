# Generated by Django 4.2.1 on 2023-06-20 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Singer',
            new_name='Student',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='gender',
            new_name='city',
        ),
        migrations.DeleteModel(
            name='Song',
        ),
    ]
