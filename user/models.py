# -*- coding: utf-8 -*-
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50, null=False, primary_key=True)  # 这个是主键
    password = models.CharField(max_length=50, null=False)
    name = models.CharField(max_length=50, null=False)  # 名称
    regtime = models.DateTimeField(auto_now=True)
    logintime = models.DateTimeField(auto_now=True)
    school = models.CharField(max_length=50, null=False, default="")
    course = models.CharField(max_length=50, null=False, default="")
    classes = models.CharField(max_length=50, null=False, default="")  # 行政班
    number = models.CharField(max_length=50, null=False, default="")
    realname = models.CharField(max_length=50, null=False)
    qq = models.CharField(max_length=50, null=True, default="")
    email = models.CharField(max_length=50, null=True, default="")
    type = models.IntegerField(null=False, default=1)  # 1 普通 2 管理员 3 超级管理员

    objects = models.Manager()

    def __str__(self):
        return self.username


class UserData(models.Model):
    username = models.CharField(max_length=50, null=False, primary_key=True)
    ac = models.IntegerField(null=False, default=0)
    submit = models.IntegerField(null=False, default=0)
    score = models.IntegerField(default=0)  # 总得分
    des = models.CharField(max_length=50, null=True)  # 介绍
    rating = models.IntegerField(default=1500)
    acpro = models.TextField(null=True, default="")  # ac的题目

    objects = models.Manager()

    def __str__(self):
        return self.username


class UserLoginData(models.Model):
    username = models.CharField(max_length=50, null=False)
    ip = models.CharField(max_length=50, null=True, default="unkonw")
    logintime = models.DateTimeField(auto_now=True)
    msg = models.TextField(null=True)  # 额外的信息，如浏览器版本等

    objects = models.Manager()

    def __str__(self):
        return self.username
