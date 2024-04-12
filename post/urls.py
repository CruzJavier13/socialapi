from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.PostView.as_view()),
    path('post/<int:pk>/', views.PostView.as_view()),
]