from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ProfessionalCareerViewset.as_view({ 'get': 'list' })),
    path('create/', views.ProfessionalCareerViewset.as_view({ 'post': 'create' })),
    path('<int:pk>/', views.ProfessionalCareerViewset.as_view({ 'get': 'retrieve', 'put':'partial_update', 'delete': 'destroy' })),
]