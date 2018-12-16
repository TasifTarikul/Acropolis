from django.urls import path, include
from .views import UserProfileViewSet
from rest_framework import routers


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('list', UserProfileViewSet, base_name='user_profile_api')


urlpatterns = [
    # path('', include(router.urls)),
    path('', include((router.urls, 'user'), namespace='user_profile_api'))
]