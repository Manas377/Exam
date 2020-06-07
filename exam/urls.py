from django.urls import path
from . import views


app_name = 'exam'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('test/', views.TestView, name='test'),
    path('test2/', views.TestView2, name='test2')
]