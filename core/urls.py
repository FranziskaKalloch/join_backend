from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('auth_app.api.urls')),
    path('api/', include('contact_app.api.urls')),
    path('api/', include('board_app.api.urls')),
    path('api/', include('summary_app.api.urls')),
    path('api/', include('tasks_app.api.urls')),
    
    # Der OpenAPI-Schema-Endpunkt (JSON/YAML)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    
    # Swagger-UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    
    # ReDoc-UI:
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
