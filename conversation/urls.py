from django.urls import path
from . import views

urlpatterns = [
    path('', views.ConversationView.as_view()),
    #path('<int:pk>', views.ConversationView.as_view()),
]