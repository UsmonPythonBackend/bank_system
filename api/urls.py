
from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewSetWeb, CourseViewSetWeb, ModulesViewSetWeb, LessonViewSetWeb, TasksViewSetWeb, GroupViewSetWeb, CategoryViewSetTelegram, CourseViewSetTelegram, ModulesViewSetTelegram, LessonViewSetTelegram, TasksViewSetTelegram, GroupViewSetTelegram
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'category-web', CategoryViewSetWeb, basename='category-web')
router.register(r'course-web', CourseViewSetWeb, basename='course-web')
router.register(r'modules-web', ModulesViewSetWeb, basename='modules-web')
router.register(r'lesson-web', LessonViewSetWeb, basename='lesson-web')
router.register(r'tasks-web', TasksViewSetWeb, basename='task-web')
router.register(r'group-web', GroupViewSetWeb, basename='group-web')
router.register(r'category-telegram', CategoryViewSetTelegram, basename='category-telegram')
router.register(r'course-telegram', CourseViewSetTelegram, basename='course-telegram')
router.register(r'modules-telegram', ModulesViewSetTelegram, basename='modules-telegram')
router.register(r'lesson-telegram', LessonViewSetTelegram, basename='lesson-telegram')
router.register(r'tasks-telegram', TasksViewSetTelegram, basename='task-telegram')
router.register(r'group-telegram', GroupViewSetTelegram, basename='group-telegram')




urlpatterns = [
    path('', include(router.urls)),
    path('api-auth-token/', obtain_auth_token),
]