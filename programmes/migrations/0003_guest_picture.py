# Generated by Django 4.1.4 on 2023-01-04 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programmes', '0002_remove_programme_date_programme_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='picture',
            field=models.ImageField(default='static/images/no_image.jpeg', upload_to='static/uploads'),
        ),
    ]
