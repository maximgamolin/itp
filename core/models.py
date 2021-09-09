from django.db import models


class Post(models.Model):

    title = models.CharField(verbose_name='Заголовок', max_length=255)
    body = models.TextField(verbose_name='Контент')
