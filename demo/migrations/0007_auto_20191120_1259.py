# Generated by Django 2.2.7 on 2019-11-20 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0006_friend_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='users',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Friend',
        ),
    ]
