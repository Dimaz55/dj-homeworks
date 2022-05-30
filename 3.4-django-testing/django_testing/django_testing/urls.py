from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from students.views import CoursesViewSet, StudentViewSet

router = DefaultRouter()
router.register("courses", CoursesViewSet, basename="courses")
router.register("students", StudentViewSet, basename="students")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/", include(router.urls)),
]
