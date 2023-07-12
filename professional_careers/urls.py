from django.urls import path
from . import views

urlpatterns = [
    path('professional-carrer/list/', views.ProfessionalCareerViewset.as_view({ 'get': 'list' })),
    path('professional-carrer/create/', views.ProfessionalCareerViewset.as_view({ 'post': 'create' })),
    path('professional-carrer/<int:pk>/', views.ProfessionalCareerViewset.as_view({ 'get': 'retrieve', 'put':'partial_update', 'delete': 'destroy' })),
]