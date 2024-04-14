from django.urls import path
from . import views

urlpatterns = [
    path('comment/', views.CommentView.as_view()),
    path('comment/<int:pk>/', views.CommentView.as_view()),
    #path('comment/update/<int:pk>', views.CommentView.as_view()),
    path('likecomment/', views.LikeCommentView.as_view()),
    path('likecomment/<int:pk>', views.LikeCommentView.as_view()),
    path('likepost/', views.LikePostView.as_view()),
    path('likepost/<int:pk>', views.LikePostView.as_view()),
]