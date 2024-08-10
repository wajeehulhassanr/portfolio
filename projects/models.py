from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='project_images/')
    # github_link = models.URLField(blank=True, null=True)
    live_demo_link = models.URLField()
    # total_users = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title