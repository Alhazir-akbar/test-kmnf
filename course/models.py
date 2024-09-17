from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


class Course(models.Model):
    course = models.CharField(max_length=50)
    mentor = models.CharField(max_length=50)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class UserCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"
