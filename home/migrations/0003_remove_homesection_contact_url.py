# Generated by Django 5.0.7 on 2024-08-06 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_remove_homesection_description"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="homesection",
            name="contact_url",
        ),
    ]
