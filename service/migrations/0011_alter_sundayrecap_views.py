# Generated by Django 4.2 on 2023-05-22 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0010_sundayrecap_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sundayrecap',
            name='views',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]