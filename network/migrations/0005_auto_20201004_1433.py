# Generated by Django 3.1.1 on 2020-10-04 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_auto_20201004_1229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='follower',
            new_name='followerCount',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='following',
            new_name='followingCount',
        ),
    ]
