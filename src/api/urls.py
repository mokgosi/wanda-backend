from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from .views import TestimonialViewSet, UserViewSet, WanderViewSet, PageViewSet

router = DefaultRouter()
router.register('testimonials', TestimonialViewSet, basename='testimonials')
router.register('wander', WanderViewSet, basename='wander')
router.register('privacy-policy', PageViewSet, basename='privacy_policy')
router.register('users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # path('testimonials/', TestimonialList.as_view()),
    # path('testimonials/<int:id>/', TestimonialDetail.as_view()),
]