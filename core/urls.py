from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homeView, name='home'),
    path('accounts/', include('accounts.urls')),
    path('profile/', include('profiles.urls')),
    path('category/', include('category.urls')),
    path('settings/', include('settings.urls')),

    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)