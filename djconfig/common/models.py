from django.db import models

class Post(models.Model):
    postname = models.CharField(max_length=50)
    contents = models.TextField()
    create_date = models.DateTimeField()
    def __str__(self):
        return self.postname

class Comment(models.Model):
    question = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()


# Create your models here.
