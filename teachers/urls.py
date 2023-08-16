from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.TeacherViewset.as_view({ 'get': 'list' })),
    path('<int:pk>/', views.TeacherViewset.as_view({ 'get': 'retrieve', 'put':'partial_update', 'delete': 'destroy' })),
]