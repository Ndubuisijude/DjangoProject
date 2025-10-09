from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.student_view, name='student_view'),
    path('come_inside/', views.come_inside, name='come_inside'),
    path('name', views.say_Name, name='say_name'),
    path('index/', views.index, name='student'),
    path('jude/', views.jude, name='jude'),
    path('family/', views.family, name='family'),
]