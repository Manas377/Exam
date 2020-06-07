from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('signup/student/', views.StudentSignUpView.as_view(), name='student-signup'),
    path('signup/teacher/', views.TeacherSignUpView.as_view(), name='teacher-signup')
]
