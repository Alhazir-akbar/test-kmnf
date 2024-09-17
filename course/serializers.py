from rest_framework import serializers
from .models import User, Course, UserCourse


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        read_only_fields = ['id']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'course', 'mentor', 'title']
        read_only_fields = ['id']


class UserCourseSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  
    course = CourseSerializer(read_only=True)    

    class Meta:
        model = UserCourse
        fields = ['id', 'user', 'course']
        read_only_fields = ['id']


class CreateUserCourseSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    class Meta:
        model = UserCourse
        fields = ['user', 'course']
