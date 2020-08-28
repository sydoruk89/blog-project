from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    rubric = models.CharField(max_length=64, null=True)
    body = models.TextField(null=True)
    time = models.DateTimeField(auto_now=True)


def __str__(self):
    return self.author