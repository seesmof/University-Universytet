from django.db import models


class HistoryItem(models.Model):
    text = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now=True, auto_now_add=False)
