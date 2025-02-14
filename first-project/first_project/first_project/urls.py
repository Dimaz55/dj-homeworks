from django.contrib import admin
from django.urls import path, include

from app.views import home_view, time_view, workdir_view


urlpatterns = [
    path('', home_view, name='home'),
    # Раскомментируйте код, чтобы данные урлы 
    # обрабатывались Django
    path('current_time/', time_view, name='time'),
    path('workdir/', workdir_view, name='workdir'),
    path('admin/', admin.site.urls),
]
