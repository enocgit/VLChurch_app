# Generated by Django 4.2 on 2023-04-22 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fellowships', '0002_alter_fellowship_meeting_days_alter_musicgroup_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fellowship',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='musicgroup',
            options={'ordering': ['name']},
        ),
    ]