# Generated by Django 4.2 on 2023-04-20 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programmes', '0013_alter_guest_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='picture',
            field=models.ImageField(upload_to='images'),
        ),
    ]