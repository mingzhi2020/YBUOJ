from rest_framework import serializers
from .models import *


class SettingTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = SettingTable
        fields = '__all__'


class DailyTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyTable
        fields = '__all__'
