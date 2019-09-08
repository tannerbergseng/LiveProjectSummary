from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length = 20)

    def __str__(self):
        return self.name


class Post(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 100)
    author = models.ForeignKey(User, on_delete = models.CASCADE) #Use Django's auth model to assign the logged in user as author
    location = models.CharField(max_length = 50)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)
    categories = models.ManyToManyField('Category', related_name = 'posts') # Categories are used as tags

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length = 50)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    post = models.ForeignKey('Post', on_delete = models.CASCADE) # There can be multiple comments to any one post

    def __str__(self):
        return self.author