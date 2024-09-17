import json
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from .models import User, Course, UserCourse
from .serializers import UserSerializer, CourseSerializer, UserCourseSerializer
from django.db.models import Count
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_view(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            username = body.get('username')
            password = body.get('password')

            if not username or not password:
                raise ValidationError("Username dan password harus disediakan.")

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                
                token, created = Token.objects.get_or_create(user=user)
                return JsonResponse({'message': 'Login successful', 'token': token.key}, status=200)
            else:
                return JsonResponse({'message': 'Invalid credentials'}, status=400)
        except ValidationError as e:
            return JsonResponse({'message': str(e)}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON'}, status=400)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    @action(detail=False, methods=['get'], permission_classes=[IsAdminUser])
    def list_users(self, request):
        users = User.objects.all()
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def filter_courses(self, request):
        course_title = request.query_params.get('title', None)
        if course_title:
            courses = Course.objects.filter(title__icontains=course_title)
        else:
            courses = Course.objects.all()

        serializer = self.get_serializer(courses, many=True)
        return Response(serializer.data)


class UserCourseViewSet(viewsets.ModelViewSet):
    serializer_class = UserCourseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if not user.is_staff:
            return UserCourse.objects.filter(user=user)
        return UserCourse.objects.all()

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def filter_user_courses(self, request):
        course_title = request.query_params.get('course_title', None)
        if course_title:
            user_courses = UserCourse.objects.filter(course__title__icontains=course_title, user=request.user)
        else:
            user_courses = UserCourse.objects.filter(user=request.user)

        serializer = self.get_serializer(user_courses, many=True)
        return Response(serializer.data)


class AdminCourseViewSet(viewsets.ViewSet):
    permission_classes = [IsAdminUser]

    @action(detail=False, methods=['get'])
    def dashboard_stats(self, request):
        total_users = User.objects.count()
        total_courses = Course.objects.count()
        user_course_stats = UserCourse.objects.values('course__title').annotate(total_users=Count('user'))

        stats = {
            'total_users': total_users,
            'total_courses': total_courses,
            'user_course_stats': list(user_course_stats)
        }

        return Response(stats, status=status.HTTP_200_OK)
