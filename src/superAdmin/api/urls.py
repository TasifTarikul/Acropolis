from django.urls import path, include
from .views import UserViewSet
from rest_framework import routers 


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('list', UserViewSet, base_name='user_api')


urlpatterns = [
    # path('', include(router.urls)),
    path('', include((router.urls, 'user'), namespace='user_api'))
]