# Generated by Django 4.2 on 2023-04-23 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fellowships', '0003_alter_fellowship_options_alter_musicgroup_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeetingDays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='day')),
            ],
        ),
        migrations.RemoveField(
            model_name='fellowship',
            name='meeting_days',
        ),
        migrations.AddField(
            model_name='fellowship',
            name='meeting_days',
            field=models.ManyToManyField(to='fellowships.meetingdays'),
        ),
    ]