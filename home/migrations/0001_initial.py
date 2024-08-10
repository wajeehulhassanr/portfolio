# Generated by Django 5.0.7 on 2024-08-06 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="HomeSection",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("title", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=255)),
                ("profile_picture", models.ImageField(upload_to="profile_pics/")),
                ("resume", models.FileField(upload_to="resumes/")),
                ("contact_url", models.URLField(default="/#contact")),
            ],
        ),
    ]
