from django.contrib import admin
from django.conf import settings  #LOAD CONFIG TO FILE
from django.conf.urls.static import static #LOAD IMAGE
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('post/', include('posts.urls')),
    path('comment/', include('comment.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
