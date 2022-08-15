from django.urls import path
from django.conf.urls import url
from .views import *
from rest_framework.routers import DefaultRouter



urlpatterns = [
     url(r'^change',UserChangeView.as_view()),
     url(r'^change_all',UserChangeAllView.as_view()),
     url(r'^register',UserRegisterAPIView.as_view()),
     url(r'^login',UserLoginAPIView.as_view()),
     url(r'^logout',UserLogoutAPIView.as_view()),
     url(r'^updaterating',UserUpdateRatingAPIView.as_view()),
     url(r'^setlogindata', UserLoginDataAPIView.as_view()),
]

router = DefaultRouter()
router.register(r'user', UserView)
router.register(r'userdata',UserDataView)
router.register(r'userlogindata',UserLoginDataView)
urlpatterns += router.urls
