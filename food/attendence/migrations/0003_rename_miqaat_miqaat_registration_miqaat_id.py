# Generated by Django 5.1.6 on 2025-03-09 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendence', '0002_remove_miqaat_registration_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='miqaat_registration',
            old_name='miqaat',
            new_name='miqaat_id',
        ),
    ]
