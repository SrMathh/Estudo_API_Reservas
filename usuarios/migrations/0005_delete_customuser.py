# Generated by Django 5.1.3 on 2024-12-05 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_user_remove_customuser_is_admin'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
