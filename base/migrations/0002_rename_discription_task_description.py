# Generated by Django 5.1.3 on 2024-12-06 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="discription",
            new_name="description",
        ),
    ]
