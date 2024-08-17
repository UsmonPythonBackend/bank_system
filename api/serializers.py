from rest_framework import serializers
from api.models import Category,Course, Modules, Lesson, Tasks, User, Group

# Web
class CategorySerializerWeb(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CourseSerializerWeb(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class ModulesSerializerWeb(serializers.ModelSerializer):
    class Meta:
        model = Modules
        fields = '__all__'


class LessonSerializerWeb(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class TasksSerializerWeb(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'


class UserSerializerWeb(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GroupSerializerWeb(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


# Telegram

class CategorySerializerTelegram(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CourseSerializerTelegram(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class ModulesSerializerTelegram(serializers.ModelSerializer):
    class Meta:
        model = Modules
        fields = '__all__'


class LessonSerializerTelegram(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class TasksSerializerTelegram(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'


class UserSerializerTelegram(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GroupSerializerTelegram(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'