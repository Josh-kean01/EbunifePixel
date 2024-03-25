
from django.contrib import admin
from django.urls import path, include
from EbunIfeProj.settings import DEBUG, MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls'))
]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
