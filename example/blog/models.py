from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    content = models.TextField()
    is_published = models.BooleanField(default=False)
