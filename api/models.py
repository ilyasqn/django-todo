from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, default='Task')
    description = models.TextField(max_length=400, null=True, default='Task description')
    completed = models.BooleanField(default='', blank=True, null=True),
    def __str__(self):
        return self.title