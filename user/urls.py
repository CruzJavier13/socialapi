from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.UserView.as_view()),
    path('user/<int:pk>/', views.UserView.as_view()),
]