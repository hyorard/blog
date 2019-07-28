from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return self.title
