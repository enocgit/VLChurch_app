# Generated by Django 4.2 on 2023-04-27 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaders', '0005_leader_ref'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leader',
            name='ref',
            field=models.CharField(default='D', max_length=1),
        ),
    ]
