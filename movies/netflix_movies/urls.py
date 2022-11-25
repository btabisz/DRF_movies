from rest_framework import routers
from .views import MovieViewSet, VoteViewSet, CategoryViewSet
from django.urls import include, path

router = routers.DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'votes', VoteViewSet)
router.register(r'category', CategoryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
