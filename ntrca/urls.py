from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ntrca_app.urls')),
    path('candidate/', include('candidate.urls')),
    path('ntrca_result/', include('ntrca_result.urls')),
    path('import/', include('import.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
