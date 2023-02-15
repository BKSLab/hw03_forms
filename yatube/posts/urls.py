from django.urls import path
from posts.apps import PostsConfig
from posts.views import (group_posts, index, post_create, post_detail,
                         post_edit, profile)

app_name = PostsConfig.name

urlpatterns = [
    path('', index, name='h_page'),
    path('group/<slug:slug>/', group_posts, name='page_post'),
    path('profile/<str:username>/', profile, name='profile'),
    path('create/', post_create, name='post_create'),
    path('posts/<int:post_id>/edit/', post_edit, name='post_edit'),
    path('posts/<int:post_id>/', post_detail, name='post_detail'),
]
