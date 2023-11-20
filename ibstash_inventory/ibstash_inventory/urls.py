from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.core.urls")),
    path("", include("apps.api.routes")),
    path("select2/", include("django_select2.urls")),
    path('hello-webpack/', TemplateView.as_view(template_name='index.html'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
