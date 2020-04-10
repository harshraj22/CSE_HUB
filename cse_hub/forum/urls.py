from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='forum-home'),
    path('post/add', views.create_post, name='create-post'),
    path('post/<int:post_id>/', views.display_post, name='display-post'),
    path('comment/<int:post_id>/', views.comment, name='comment'),
    path('delete/comment/<int:comment_id>/', views.delete_comment, name='delete-comment')
]