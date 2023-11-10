from django.db import models
# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from googletrans import Translator
from bs4 import BeautifulSoup
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _




User = get_user_model()

translator = Translator(service_urls=[
            'translate.google.com',
            'translate.google.co.kr',
        ])


class StudyingTime(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField( null=True, unique=True)
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Время обучения'
        verbose_name_plural = 'Время обучения'







class CourseForLanding(models.Model):
    title = models.CharField(max_length=123, verbose_name=('Название'))
    slug = models.SlugField(null=True, unique=True)
    cover = models.ImageField(upload_to='media/image/', verbose_name=('Обложка'))
    description = models.TextField(verbose_name=('Описание о языке'))
    studying_time = models.ManyToManyField(StudyingTime, verbose_name='Время обучения')
    format = models.ManyToManyField('srm.LearningFormat', verbose_name='Формат обучения')
    additional_info = models.TextField(verbose_name='Информация о курсе', blank=True, null=True)
    teacher = models.ForeignKey('srm.Employee', on_delete=models.PROTECT, verbose_name='Ментор')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=('Дата создания'))
    is_active = models.BooleanField(default=True, verbose_name=('Активен'))

   
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс для Лэндинга'
        verbose_name_plural = 'Курс для Лэндинга'


class Review(models.Model):
    name = models.CharField(max_length=70, verbose_name='Имя')
    slug = models.SlugField(null=True, unique=True)
    direction = models.CharField(max_length=50, verbose_name='Направление')
    description = models.TextField(verbose_name=('Описание'), max_length=515)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=('Дата создания'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Section(models.Model):
    title = models.CharField(max_length=123, verbose_name='Название')
    slug = models.SlugField(null=True, unique=True)
    id_section = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
    description = models.TextField(verbose_name='Описание для подраздела', blank=True, null=True)
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
   


class Article(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Ментор'))
    topic_name = models.CharField(max_length=80, verbose_name=_('Название темы'))
    slug = models.SlugField(blank=True, null=True, unique=True)
    body = RichTextField(verbose_name=_('Контент'))
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name=_('Раздел'))
    created_date = models.DateField(auto_now_add=True, verbose_name=_('Дата создания')) 

    def __str__(self):
        return self.topic_name

    
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'




class SubscriptionToCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    slug = models.SlugField(null=True, unique=True)
    phone_number = models.CharField(verbose_name=('Номер телефона'), max_length=15, null=True)

    course = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name='Курс')
    created_date = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return str(self.user)




    class Meta:
        verbose_name = 'Подписка на курс'
        verbose_name_plural = 'Подписка на курс'
        unique_together = ['user', 'course']













