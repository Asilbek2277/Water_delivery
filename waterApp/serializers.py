from rest_framework import serializers
from .models import *


class SuvSerializer(serializers.ModelSerializer):
    class Meta:
        model=Suv
        fields="__all__"

    def validate_litr(self, value):
        if int(value) > 19:
            raise serializers.ValidationError("Kechirasiz bunday katta litrdagi suz sotilmaydi!!!")
        return value


class MijozSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mijoz
        fields = "__all__"


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = "__all__"

    def validate_yosh(self, value):
        if int(value) > 19:
            raise serializers.ValidationError("Yoshingiz mos kelmaydi!!!")
        return value


class HaydovchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Haydovchi
        fields = "__all__"


class BuyurtmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyurtma
        fields = "__all__"

    def validate_mijoz__qarz(self, value):
        if int(value) > 500000:
            raise serializers.ValidationError("Qarzingiz jida ko'p buyurtma qila olmaysiz!!!")
        return value

