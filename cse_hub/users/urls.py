from django.urls import path
from . import views 

urlpatterns = [
    path('', views.profile, name='user-profile'),
    path('edit', views.profile_edit, name='user-profile-edit'),
]
