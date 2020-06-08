from django.urls import path
from . import views


app_name = 'exam'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('test/', views.TestView.as_view(), name='test'),
]