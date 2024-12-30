"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework.authtoken import views
admin_urls = [
    path('api/admin/users/',
         include(('config.auths.users.urls.admin', 'config.auths.users'), namespace='users-admin')),

    path('api/admin/catalog/',
         include(('config.apps.catalog.urls.admin', 'config.apps.catalog'), namespace='catalog-admin')),
]

front_urls = [
    path('api/front/users/',
         include(('config.auths.users.urls.front', 'config.auths.users'), namespace='users-front')),
    path('api/front/catalog/',
         include(('config.apps.catalog.urls.front', 'config.apps.catalog'), namespace='catalog-front')),
]

doc_patterns = [
    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
urlpatterns = [
                  path('admin/', admin.site.urls),


              ] + front_urls + admin_urls + doc_patterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_title = 'DjShop'
admin.site.site_header = 'DjShop'
admin.site.index_title = 'DjShop'
