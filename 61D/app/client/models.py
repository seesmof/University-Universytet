from django.db import models


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(blank=True)  # optional
    due = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} due {self.due.strftime("%d/%m/%Y")}"
