
from django.shortcuts import render
from rest_framework import viewsets, authentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import PaymentCourse
from .serializers import PaymentCourseSerializerWeb, PaymentCourseSerializerTelegram


class PaymentCourseViewSetWeb(viewsets.ModelViewSet):
    serialize_class = PaymentCourseSerializerWeb
    permission_classes =[IsAuthenticated]
    authentication_classes =[authentication.TokenAuthentication]



class PaymentCourseViewSetTelegram(viewsets.ModelViewSet):
    serialize_class = PaymentCourseSerializerTelegram
    permission_classes =[IsAuthenticated]
    authentication_classes =[authentication.TokenAuthentication]

