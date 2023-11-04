from django.urls import path
from . import views

urlpatterns = [
    path('api/start-camera', views.start_camera),
    path('api/stop-camera', views.stop_camera),
    path('', views.index_view),
]
