# Generated by Django 4.2 on 2023-04-19 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programmes', '0006_alter_guest_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='picture',
            field=models.ImageField(default='static/images/no-image.png', upload_to='media/images'),
        ),
    ]
