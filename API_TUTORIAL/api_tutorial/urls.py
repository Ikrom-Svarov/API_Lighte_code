from django.urls import path
from .views import SectionCreate, ArticleCreate, ArticleList, ArticleRetrieve


urlpatterns = [
    path('SectionCreate/', SectionCreate.as_view()),
    path('ArticleList/', ArticleList.as_view()),
    path('ArticleCreate/', ArticleCreate.as_view()),
    path('ArticleRetrieve/<slug:slug>/', ArticleRetrieve.as_view()),
    
]