# Generated by Django 4.0.3 on 2022-03-25 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='userfollowing',
            name='unique follower/following',
        ),
    ]
