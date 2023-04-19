# Generated by Django 4.2 on 2023-04-19 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_alter_member_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='picture',
            field=models.ImageField(blank=True, default='/static/images/no_image.jpeg', null=True, upload_to='static/uploads'),
        ),
    ]
