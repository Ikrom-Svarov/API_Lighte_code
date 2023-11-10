from django.db import models
from ckeditor.fields import RichTextField

class Section(models.Model):
    title = models.CharField(max_length=123, verbose_name='Название')
    slug = models.SlugField(unique=True)
    id_section = models.ForeignKey('self', on_delete=models.CASCADE,  null=True, related_name='children')
    description = models.TextField(verbose_name='Описание для подраздела',  null=True)
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'


class Article(models.Model):
    topic_name = models.CharField(max_length=80, verbose_name='Название темы')
    slug = models.SlugField(unique=True)
    body = RichTextField(verbose_name='Контент')
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name='Раздел')
    created_date = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.topic_name

    
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'