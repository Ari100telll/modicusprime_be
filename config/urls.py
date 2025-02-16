"""modicusprime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


urlpatterns = [
    # Django Admin, use {% url 'admin:index' %}
    path('admin/', admin.site.urls),
    # path("", HealthCheckView.as_view(), name="health_check"),
    # path("health/", HealthCheckView.as_view(), name="health_check"),
    # path("version/", VersionView.as_view(), name="version"),
    # Open API Schema
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    # Swagger and Redoc UI
    path(
        "schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    # Your stuff: custom urls includes go here
]
# API URLS
urlpatterns += [
    # API base urls
    path("api/", include("config.api_router")),
    path("api/auth/", include("rest_framework.urls", namespace="rest_framework")),
]
