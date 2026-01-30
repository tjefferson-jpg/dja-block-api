from django.db import models

# Create your models here.
from django.db import models
from  django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, related_name='articles')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return {'title':self.title, 'content':self.content, 'author':self.author}


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)