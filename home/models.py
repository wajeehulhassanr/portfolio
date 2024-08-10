from django.db import models


class HomeSection(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    # description = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='profile_pics/')
    resume = models.FileField(upload_to='resumes/')
    # contact_url = models.URLField(default='/#contact')

    def __str__(self):
        return self.name