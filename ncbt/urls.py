from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

handler404 = "app_main.views.custom_page_not_found_view"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("student_portal/", include("std_portal.urls")),
    path("", include("app_main.urls", "app_main")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
