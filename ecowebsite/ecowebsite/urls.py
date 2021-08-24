
import website
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    path('ckeditor', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('', include('website.urls', namespace='website')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_URL}),
    
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)