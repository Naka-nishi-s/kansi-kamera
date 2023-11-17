from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from .views import CustomLoginView  # カスタムログインビューをインポート

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login', CustomLoginView.as_view()),  # ログインAPI
    path('api/', include('watch_room.urls')),  # watch_roomアプリのAPIエンドポイント
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),  # Reactアプリへのルーティング
]
