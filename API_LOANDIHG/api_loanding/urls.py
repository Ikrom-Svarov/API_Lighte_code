from django.urls import path, include
from .views import CourseForLandingList,  CourseFoLandingRetrieve, CourseForLandingCreate
from .views import  ReviewList, EmployeeList, EmployeeRetrieve, ReviewCreate
from.views import  SubscriptionToCourseList,  SubscriptionToCourseRetrieve
urlpatterns = [

 


    path('CourseForLandingList/', CourseForLandingList.as_view() ),
    path('CourseForLandingRetrieve/<slug:slug>/', CourseFoLandingRetrieve.as_view()  ),
    path('CourseForLandingCreate/', CourseForLandingCreate.as_view()),


    path('ReviewList', ReviewList.as_view()),
    path('ReviewCreate/', ReviewCreate.as_view()),




    path('SubscriptionToCourseList', SubscriptionToCourseList.as_view()),
    path('SubscriptionToCourseRetrieve/<slug:slug>/', SubscriptionToCourseRetrieve.as_view()),
    


    path('EmployeeList', EmployeeList.as_view()),
    path('EmployeeRetrieve/<slug:slug>/', EmployeeRetrieve.as_view()),
    


    
]