# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import CreateAPIView, ListCreateAPIView, \
    RetrieveUpdateAPIView

from .models import Sensor, Measurement
from .serializers import (
    ListCreateSensorSerializer,
    RetrieveUpdateSensorSerializer,
    CreateMeasurementSerializer
)


class ListCreateSensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = ListCreateSensorSerializer


class RetrieveUpdateSensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = RetrieveUpdateSensorSerializer


class CreateMeasurementView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = CreateMeasurementSerializer
