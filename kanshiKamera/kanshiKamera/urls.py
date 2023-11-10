from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
# from django.views.generic import TemplateView
# from django.contrib.auth import views as auth_views
from .views import CustomLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login', CustomLoginView.as_view()),
    path('', include("watch_room.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)