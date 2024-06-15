from rest_framework import routers
from django.urls import path, include

drf_default_router = routers.DefaultRouter()

urlpatterns = [
    path('certiffy/', include('certiffy.urls')),
    # path('base/', include('base.urls')),
    # path('features/', include('features.urls')),
    # path('metadata/', include('metadata.urls')),
    path('resources/', include('resources.urls')),
]

urlpatterns += drf_default_router.urls
