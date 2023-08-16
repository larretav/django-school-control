from django.urls import path
from . import views

urlpatterns = [
    #AUTH
    path('login/', views.token),
    path('token/refresh/', views.refresh_token),
    path('logout/', views.revoke_token),

    #USER CURRENT
    path('users/current/', views.UserProfile.as_view(), name='users'),
    path('register/students/', views.UserAccountStudentRegisterView.as_view(), name='register Students'),
    path('register/teachers/', views.UserAccountTeacherRegisterView.as_view(), name='register Teachers'),

    #PASSWORD CHANGE
    path('password/change/', views.update_user_password),
]