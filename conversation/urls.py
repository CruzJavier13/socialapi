from django.urls import path
from . import views

urlpatterns = [
    path('conversation/', views.ConversationView.as_view()),
    path('conversation/<int:pk>/', views.ConversationView.as_view()),
]