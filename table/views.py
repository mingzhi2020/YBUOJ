from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.pagination import LimitOffsetPagination
from .serializers import *
from .permission import ManagerOnly
from .models import *
import datetime

class SettingTableView(viewsets.ModelViewSet):
    queryset = SettingTable.objects.all()
    serializer_class = SettingTableSerializer
    permission_classes = (ManagerOnly,)
    throttle_scope = "post"
    throttle_classes = [ScopedRateThrottle, ]


class DailyTableView(viewsets.ModelViewSet):
    queryset = DailyTable.objects.filter(collecttime__gte=datetime.datetime.now(
    )-datetime.timedelta(days=10)).order_by('collecttime') # 这里有bug，不应该在queryset里写filter。时间会提前算好，导致不准确
    serializer_class = DailyTableSerializer
    filter_fields = ('username', 'collecttime')
    pagination_class = LimitOffsetPagination
    permission_classes = (ManagerOnly,)
    throttle_scope = "post"
    throttle_classes = [ScopedRateThrottle, ]
