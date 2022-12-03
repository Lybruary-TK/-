from rest_framework.routers import DefaultRouter
from lms.views import StudentViewSet, CuratorViewSet, GroupViewSet, DirectionViewSet

lms_router = DefaultRouter()
lms_router.register(r'student', StudentViewSet, basename='user')
lms_router.register(r'curator', CuratorViewSet, basename='curator')
lms_router.register(r'group', GroupViewSet, basename='group')
lms_router.register(r'direction', DirectionViewSet, basename='direction')
