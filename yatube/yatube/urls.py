from about.apps import AboutConfig
from django.contrib import admin
from django.urls import include, path
from posts.apps import PostsConfig
from users.apps import UsersConfig

urlpatterns = [
    path('', include('posts.urls', PostsConfig.name)),
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls', UsersConfig.name)),
    path('auth/', include('django.contrib.auth.urls')),
    path('about/', include('about.urls', AboutConfig.name)),
]
