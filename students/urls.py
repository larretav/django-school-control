from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.StudentViewset.as_view({ 'get': 'list' })),
    path('create/', views.StudentViewset.as_view({ 'post': 'create' })),
    path('<int:pk>/', views.StudentViewset.as_view({ 'get': 'retrieve', 'put':'partial_update', 'delete': 'destroy' })),
]