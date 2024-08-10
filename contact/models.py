from django.db import models

class ContactInfo(models.Model):
    email = models.EmailField()
    linkedin_url = models.URLField()

    def __str__(self):
        return self.email