from django.db import models


class TodoItem(models.Model):
    label = models.CharField(max_length=255)
    done = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.label
