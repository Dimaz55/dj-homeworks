from django.urls import path

from calculator.views import calc, DATA

urlpatterns = [path(key+'/', calc) for key in DATA.keys()]
