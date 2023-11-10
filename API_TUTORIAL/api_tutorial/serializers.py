from .models import Section, Article
from rest_framework import serializers


class ToSection(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['title']

class UserSection(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['id_section']

class ApiSection(serializers.ModelSerializer):

    class Meta:
        model = Section
        fields = '__all__'

    def to_representation(self,instance):
        representation =  super().to_representation(instance)
        representation['id_section'] = UserSection(instance.id_section).data
        return representation
    

class ApiArticle(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

    def to_representation(self, instance):
        representation =  super().to_representation(instance)    
        representation['section'] = ToSection(instance.section).data
        return representation