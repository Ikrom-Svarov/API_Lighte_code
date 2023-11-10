from django.contrib import admin
from .models import StudyingTime, CourseForLanding, Review, Section, Article, SubscriptionToCourse

# Register your models here.
admin.site.register(StudyingTime),
admin.site.register(CourseForLanding),
admin.site.register(Review),
admin.site.register(Section),
admin.site.register(Article),
admin.site.register(SubscriptionToCourse),