from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CourseViewSet, UserCourseViewSet, AdminCourseViewSet, login_view

# Buat router untuk mendaftarkan ViewSet
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'courses', CourseViewSet, basename='courses')
router.register(r'user-courses', UserCourseViewSet, basename='user-courses')

# Route khusus untuk admin dashboard
admin_router = DefaultRouter()
admin_router.register(r'admin/dashboard', AdminCourseViewSet, basename='admin-dashboard')

urlpatterns = [
    path('api/', include(router.urls)),           # URL untuk users, courses, dan user-courses
    path('api/', include(admin_router.urls)),     # URL untuk admin dashboard
    path('api/login/', login_view, name='login'),
]
