from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.SchoolGroupViewset.as_view({ 'get': 'list' })),
    path('create/', views.SchoolGroupViewset.as_view({ 'post': 'create' })),
    path('<int:pk>/', views.SchoolGroupViewset.as_view({ 'get': 'retrieve', 'put':'partial_update', 'delete': 'destroy' })),
]