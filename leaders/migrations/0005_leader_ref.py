# Generated by Django 4.2 on 2023-04-27 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaders', '0004_alter_leadertitle_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='leader',
            name='ref',
            field=models.CharField(default='A', max_length=2),
        ),
    ]
