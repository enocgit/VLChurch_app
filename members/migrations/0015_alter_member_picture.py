# Generated by Django 4.2 on 2023-04-20 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0014_alter_member_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
