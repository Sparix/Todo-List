from django.db import models


class Tags(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField(blank=True)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    is_completed = models.BooleanField()
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE)
