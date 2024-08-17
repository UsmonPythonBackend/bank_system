from django.shortcuts import render
from rest_framework import viewsets, authentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Category, Course, Modules, Lesson, Tasks, User, Group
from .serializers import *



class CategoryViewSetWeb(viewsets.ModelViewSet):
    serialize_class = CategorySerializerWeb
    permission_classes =[IsAuthenticated]
    authentication_classes =[authentication.TokenAuthentication]


class CourseViewSetWeb(viewsets.ModelViewSet):
    serializer_class = CourseSerializerWeb
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]


class ModulesViewSetWeb(viewsets.ModelViewSet):
    serializer_class = ModulesSerializerWeb
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]


class LessonViewSetWeb(viewsets.ModelViewSet):
    serializer_class = LessonSerializerWeb
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]


class TasksViewSetWeb(viewsets.ModelViewSet):
    serializer_class = TasksSerializerWeb
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]


class GroupViewSetWeb(viewsets.ModelViewSet):
    serializer_class = GroupSerializerWeb
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]


# tekegram

class CategoryViewSetTelegram(viewsets.ModelViewSet):
    serialize_class = CategorySerializerTelegram
    permission_classes =[IsAuthenticated]
    authentication_classes =[authentication.TokenAuthentication]


class CourseViewSetTelegram(viewsets.ModelViewSet):
    serializer_class = CourseSerializerTelegram
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]


class ModulesViewSetTelegram(viewsets.ModelViewSet):
    serializer_class = ModulesSerializerTelegram
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]


class LessonViewSetTelegram(viewsets.ModelViewSet):
    serializer_class = LessonSerializerTelegram
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]


class TasksViewSetTelegram(viewsets.ModelViewSet):
    serializer_class = TasksSerializerTelegram
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]


class GroupViewSetTelegram(viewsets.ModelViewSet):
    serializer_class = GroupSerializerTelegram
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]