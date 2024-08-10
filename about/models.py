from django.db import models

# Create your models here.
# about/models.py
from django.db import models

class AboutSection(models.Model):
    profile_picture = models.ImageField(upload_to='about_pics/')
    # experience_icon = models.ImageField(upload_to='icons/')
    # education_icon = models.ImageField(upload_to='icons/')
    experience_text = models.CharField(max_length=255)
    education_text = models.CharField(max_length=255)
    about_text = models.TextField()

    def __str__(self):
        return "About Section"