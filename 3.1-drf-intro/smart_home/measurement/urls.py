from django.urls import path

from .views import (
    RetrieveUpdateSensorView,
    ListCreateSensorView,
    CreateMeasurementView
)

urlpatterns = [
    path('sensors/<pk>/', RetrieveUpdateSensorView.as_view()),
    path('sensors/', ListCreateSensorView.as_view()),
    path('measurements/', CreateMeasurementView.as_view())
]
