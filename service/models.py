from pyexpat import model
from ssl import create_default_context
from django.db import models
from django.urls import reverse


class Post(models.Model):
    
    title = models.CharField (verbose_name = 'Название', max_length = 100)
    describtion = models.TextField (verbose_name = 'Описание', null = True, blank = True)
    image = models.ImageField (verbose_name = 'Картинка', null=True, blank=True)
    created_at = models.DateTimeField (verbose_name = 'Создано', auto_now_add = True)
    updated_at = models.DateTimeField (verbose_name = 'Отредактировано', auto_now = True)
    
    def __str__(self):
        return f'{self.title}'
    
    def get_absolute_url(self):
        return reverse("index")
    

class Comment (models.Model):
    
    describtion = models.TextField (verbose_name = 'Описание', null = True, blank = True)
    post = models.ForeignKey (Post, related_name = 'comments', on_delete = models.CASCADE)
    created_at = models.DateTimeField (verbose_name = 'Создано', auto_now_add = True)

    def __str__(self):
        return f'{self.describtion}'
    
    def get_absolute_url(self):
        return reverse("index")
