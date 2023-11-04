from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nice/', include("nice.urls")),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('', include("watch_room.urls")),
]
