from django.shortcuts import render
from .serializers import ApiSection, ApiArticle
from rest_framework.generics import CreateAPIView , ListAPIView , RetrieveUpdateDestroyAPIView
from .models import Section, Article
# Create your views here.

class SectionCreate(CreateAPIView):
    queryset = Section.objects.all()
    serializer_class = ApiSection
    

class ArticleList(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ApiArticle

class ArticleCreate(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ApiArticle

class ArticleRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ApiArticle
    lookup_field = 'slug'

