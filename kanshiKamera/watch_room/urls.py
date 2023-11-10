from django.urls import path
from . import views

urlpatterns = [
    path('start-camera', views.start_camera),
    path('stop-camera', views.stop_camera),
    path('videos/', views.video_list_api),
    path('videos/<str:video_id>', views.video_detail_api),
]