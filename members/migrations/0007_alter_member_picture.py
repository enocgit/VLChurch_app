# Generated by Django 4.2 on 2023-04-19 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_alter_member_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='picture',
            field=models.ImageField(blank=True, default='static/images/no-image.png', null=True, upload_to='media'),
        ),
    ]
