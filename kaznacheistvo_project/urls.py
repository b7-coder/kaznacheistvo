from django.contrib import admin
from django.urls import path
from kaznacheistvo_site.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='main'),
    path('news/', news, name='news'),
    path('newsDetails/<int:id>', newsDetails, name='newsDetails'),
    path('support/', supportPage, name='support'),
    path('chat/', chat, name='chat'),
]


urlpatterns += static(settings.MEDIA_URL,
document_root = settings.MEDIA_ROOT)