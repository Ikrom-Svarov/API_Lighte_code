from rest_framework import serializers
from .models import StudyingTime,CourseForLanding, Review, Section, Article, SubscriptionToCourse

from django.contrib.auth.models import User 
from srm.models import Employee, LearningFormat, Course

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']




class Api_Studyingtime(serializers.ModelSerializer):
    class Meta:
        model = StudyingTime
        fields  = '__all__'
    





class UserSerializersTeacher(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['full_name']

class UserSerializersFormat(serializers.ModelSerializer):
    class Meta:
        model = LearningFormat
        fields = '__all__'

class UserTime(serializers.ModelSerializer):
    class Meta:
        model = StudyingTime
        fields = ['title']

class Api_CourseForlanding(serializers.ModelSerializer):
    # teacher = serializers.PrimaryKeyRelatedField(default=serializers.CurrentUserDefault(), read_only=True)
    # format = UserSerializersFormat(many = True)
    # studying_time = UserTime(many=True)


    class Meta:
        model = CourseForLanding
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['teacher'] = UserSerializersTeacher(instance.teacher).data 
        representation['format'] = UserSerializersFormat(instance.format.all(), many=True).data  
        representation['studying_time'] = UserSerializersFormat(instance.studying_time.all(), many=True).data  

        return representation
       


   







class Api_Review(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'





class Api_Section(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'

   


    
class Api_Article(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'




class UserCourse(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['title']

class Api_SubscriptionToCourse(serializers.ModelSerializer):
    class Meta:
        model  = SubscriptionToCourse
        fields  = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializers(instance.user).data  
        representation['course'] = UserCourse(instance.course).data  

        return representation
    




class UserCourseEmployee(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['title']

class Api_Employee(serializers.ModelSerializer):
    

    class Meta:
        model = Employee
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['studying_time'] = UserTime(instance.studying_time.all(), many=True).data
        representation['course'] = UserCourseEmployee(instance.course.all(), many = True).data
        representation['format'] = UserSerializersFormat(instance.course.all(), many = True).data

        return representation