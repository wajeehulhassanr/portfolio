from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=50)  # E.g., 'Experienced', 'Intermediate', 'Basic'

    def __str__(self):
        return self.name

class ExperiencePanel(models.Model):
    title = models.CharField(max_length=100)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.title