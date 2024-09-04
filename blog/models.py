from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=60, unique=True)


class Post(models.Model):
    STATUS = (
        (0, "Draft"),
        (1, "Published"),
    )

    title = models.CharField(max_length=255, unique=True)
    # related_name="posts" defines the reverse relation
    tags = models.ManyToManyField("Tag", related_name="posts")
    # auto_now_add=True automatically updates the value to current date time
    # when the object is first created
    created_on = models.DateTimeField(auto_now_add=True)
    # auto_now=True automatically updates the value to current date time
    # whenever the object is saved
    last_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    status = models.IntegerField(choices=STATUS, default=0)

    # metadata
    class Meta:
        ordering = ["-created_on"]

    # default human-readable representation
    def __str__(self):
        return self.title
