# Generated by Django 4.2 on 2023-04-27 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programmes', '0033_alter_programme_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='programme',
            options={'ordering': ['datetime']},
        ),
    ]