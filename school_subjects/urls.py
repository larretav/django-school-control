from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.SchoolSubjectViewset.as_view({ 'get': 'list' })),
    path('create/', views.SchoolSubjectViewset.as_view({ 'post': 'create' })),
    path('<int:pk>/', views.SchoolSubjectViewset.as_view({ 'get': 'retrieve', 'put':'partial_update', 'delete': 'destroy' })),
]