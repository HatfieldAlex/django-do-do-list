from django.db import models

# Create your models here.
class Task(models.Model):
    item = models.CharField(max_length=200)
    completion_status = models.BooleanField(default=False)

    def __str__(self):
        return self.item