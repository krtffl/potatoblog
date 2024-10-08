from django.contrib.auth.models import User
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.name


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
    content = models.TextField()

    # metadata
    class Meta:
        ordering = ["-created_on"]

    # default human-readable representation
    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=60)
    email = models.EmailField()
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    validated = models.BooleanField(default=False)

    # metadata
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return "Comment {} by {}".format(self.content, self.name)
