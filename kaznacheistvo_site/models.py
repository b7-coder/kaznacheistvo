from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class NewsDetails(models.Model):
    newsObject = models.ForeignKey(News, on_delete=models.CASCADE)
    text = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Детали новости: {self.newsObject}"

class NewsImages(models.Model):
    newsObject = models.ForeignKey(News, on_delete=models.CASCADE)
    description = models.CharField(max_length=256)
    image = models.ImageField(null=True)