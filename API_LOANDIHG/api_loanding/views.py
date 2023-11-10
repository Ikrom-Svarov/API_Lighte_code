from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from .models import StudyingTime, CourseForLanding, Review, Section, Article, SubscriptionToCourse
from srm.models import Employee
from .serializers import Api_Studyingtime, Api_CourseForlanding, Api_Review, Api_Section, Api_Article, Api_SubscriptionToCourse, Api_Employee
# Create your views here.


class CourseForLandingList(ListAPIView):
    queryset = CourseForLanding.objects.all()
    serializer_class  = Api_CourseForlanding


class CourseForLandingCreate(CreateAPIView):
    queryset =  CourseForLanding.objects.all()
    serializer_class  = Api_CourseForlanding


class CourseFoLandingRetrieve(RetrieveAPIView):
    queryset = CourseForLanding.objects.all()
    serializer_class = Api_CourseForlanding
    lookup_field = 'slug'
    
    



class ReviewList(ListAPIView):
    queryset  =  Review.objects.all()
    serializer_class = Api_Review

class ReviewCreate(CreateAPIView):
    queryset  = Review.objects.all()
    serializer_class =  Api_Review






  



class SubscriptionToCourseList(ListAPIView):
    queryset  = SubscriptionToCourse.objects.all()
    serializer_class = Api_SubscriptionToCourse

class SubscriptionToCourseCreate(CreateAPIView):
    queryset =  SubscriptionToCourse.objects.all()
    serializer_class = Api_SubscriptionToCourse


class SubscriptionToCourseRetrieve(RetrieveAPIView):
    queryset = SubscriptionToCourse.objects.all()
    serializer_class =  Api_SubscriptionToCourse
    lookup_field  = 'slug'
                                   




class EmployeeList(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = Api_Employee

class EmployeeCreate(CreateAPIView):
    queryset  =  Employee.objects.all()
    serializer_class = Api_Employee

class EmployeeRetrieve(RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = Api_Employee
    lookup_field = 'slug'
    