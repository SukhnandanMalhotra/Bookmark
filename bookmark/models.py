from django.contrib.auth.models import User
from django.db import models


class Tags(models.Model):

    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Bookmark(models.Model):

    name = models.CharField(max_length=50)
    url = models.URLField()
    is_public = models.BooleanField(default=True)
    date_time_posted = models.DateTimeField(auto_now_add=True, verbose_name="posted at")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)

    def __str__(self):
        return self.name





