# Generated by Django 4.2 on 2023-05-22 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0009_alter_sundayservice_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='sundayrecap',
            name='views',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
