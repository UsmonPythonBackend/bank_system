from rest_framework import serializers
from payment.models import PaymentCourse

class PaymentCourseSerializerWeb(serializers.ModelSerializer):
    class Meta:
        model = PaymentCourse
        fields = '__all__'


class PaymentCourseSerializerTelegram(serializers.ModelSerializer):
    class Meta:
        model = PaymentCourse
        fields = '__all__'
