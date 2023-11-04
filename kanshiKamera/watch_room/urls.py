from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view),
    path('api/start-camera', views.start_camera),
    path('api/stop-camera', views.stop_camera),
]
