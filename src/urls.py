from django.contrib import admin
from django.conf import settings  #LOAD CONFIG TO FILE
from django.conf.urls.static import static #LOAD IMAGE
from .views import LoginView
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name='login'),
    path('socialapi/', include('user.urls')),
    path('socialapi/', include('post.urls')),
    path('socialapi/', include('comment.urls')),
    path('socialapi/', include('conversation.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
