from django.urls import path
from . import views 

urlpatterns = [
    path('', views.problems, name='all-problems'),
    path('add', views.add_problem, name='add-problem'),
    path('display/<int:id>', views.display_problem, name='display-problem'),
    path('add/testcase/', views.add_testcase, name='add-testcase'),
    path('submit/<int:id>/', views.submit, name='submit-solution'),
]
