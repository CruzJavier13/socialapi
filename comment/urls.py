from django.urls import path
from . import views

urlpatterns = [
    path('comment/', views.CommentView.as_view()),
    path('comment/<int:pk>/', views.CommentView.as_view()),
]