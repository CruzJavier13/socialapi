from django.contrib import admin
from django.conf import settings  #LOAD CONFIG TO FILE
from django.conf.urls.static import static #LOAD IMAGE
from .views import LoginView
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name='login'),
    path('user/', include('user.urls')),
    path('user/<int:pk>/', include('user.urls')),
    path('post/', include('post.urls')),
    path('post/<int:pk>/', include('post.urls')),
    path('comment/', include('comment.urls')),
    path('comment/<int:pk>/', include('comment.urls')),
    path('conversation/', include('conversation.urls')),
    path('conversation/<int:pk>/', include('conversation.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
