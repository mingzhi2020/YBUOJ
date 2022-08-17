
# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from . import views
from rest_framework import routers


routers = routers.DefaultRouter()
routers.register('settingtable', views.SettingTableView)
routers.register('dailytable', views.DailyTableView)

urlpatterns = [
    url('', include(routers.urls)),
]