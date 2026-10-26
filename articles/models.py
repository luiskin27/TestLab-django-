from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='заголовок')
    content = models.TextField(verbose_name='текст статьи')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title