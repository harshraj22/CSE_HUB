from django.urls import path
from . import views 

urlpatterns = [
    path('', views.problems, name='all-problems'),
    path('add', views.add_problem, name='add-problem'),
]
