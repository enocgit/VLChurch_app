# Generated by Django 4.2 on 2023-04-24 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0024_alter_member_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='picture',
            field=models.ImageField(blank=True, default='images/no_image.png', null=True, upload_to='images'),
        ),
    ]
