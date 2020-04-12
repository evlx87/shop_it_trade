from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    re_path(r'^', include('backend.apps.mainapp.urls', namespace='main')),
    re_path(r'^auth/', include('backend.apps.authapp.urls', namespace='auth')),
    re_path(r'^basket/', include('backend.apps.basketapp.urls', namespace='basket')),
    re_path(r'^admin_panel/', include('backend.apps.adminapp.urls', namespace='admin_panel')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
