from django.contrib import admin
from .models import Course, UserCourse

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course', 'mentor', 'title')

@admin.register(UserCourse)
class UserCourseAdmin(admin.ModelAdmin):
    list_display = ('user', 'course')
    list_filter = ('user', 'course')
