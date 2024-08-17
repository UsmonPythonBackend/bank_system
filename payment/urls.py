from django.urls import path, include
from rest_framework import routers
from .views import PaymentCourseViewSetWeb, PaymentCourseViewSetTelegram
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'payment-web', PaymentCourseViewSetWeb, basename='payment-web')
router.register(r'payment-telegram', PaymentCourseViewSetTelegram, basename='payment-telegram')



urlpatterns = [
    path('', include(router.urls)),
    path('payment-auth-token/', obtain_auth_token),
]