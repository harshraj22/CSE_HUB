from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.profile, name='user-profile'),
    path('edit', views.profile_edit, name='user-profile-edit'),
]
