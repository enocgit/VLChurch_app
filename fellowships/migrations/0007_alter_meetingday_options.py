# Generated by Django 4.2 on 2023-04-23 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fellowships', '0006_rename_meetingdays_meetingday'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meetingday',
            options={'ordering': ['id']},
        ),
    ]
