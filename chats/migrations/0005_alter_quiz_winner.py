# Generated by Django 4.2 on 2023-04-22 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0004_alter_comment_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='winner',
            field=models.ManyToManyField(to='chats.winner', verbose_name='select winner(s)'),
        ),
    ]
