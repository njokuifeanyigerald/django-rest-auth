from django.urls import path, include
from rest_framework import routers
from .views import Home


router = routers.DefaultRouter()
router.register
router.register('rest', Home)

urlpatterns = [
    path('api', include(router.urls)),
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),


    # path('auth/', include('dj_rest_auth.urls')),
    # path('registration/', include('dj_rest_auth.registration.urls')),


    # path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]
