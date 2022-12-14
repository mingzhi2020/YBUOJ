from django.db import models


# 保存OJ的设置
class SettingTable(models.Model):
    schoolname = models.CharField(default="宜宾学院", max_length=100)
    ojname = models.CharField(default="YBUOJ", max_length=100)
    openwiki = models.BooleanField(default=True)
    openlanguage = models.CharField(max_length=500, default="C++|C|Python3|Python2|Swift5.1|Java")
    openoi = models.BooleanField(default=True)
    openstatus = models.BooleanField(default=True)  # 是否开启代码

    openvisitor = models.BooleanField(default=True)  # 是否开启游客访问
    openregister = models.BooleanField(default=True)  # 是否开启注册
    openselfstatus = models.BooleanField(default=True)  # 自己是否能查看自己的代码

    objects = models.Manager()

    def __str__(self):
        return self.schoolname


# class table(models.Model):
#     username = models.CharField(max_length=50, primary_key=True)
#     classes = models.CharField(max_length=50, default="")
#     number = models.CharField(max_length=50, default="")
#     OJCount = models.IntegerField(default=4)
#     OJ = models.CharField(
#         max_length=50, default="Codeforces|HDU|Vjudge|LPOJ|Others")
#     account = models.CharField(max_length=50, default="###|###|###|###|###")
#     acnum = models.CharField(max_length=50, default="0|0|0|0|0")
#     submitnum = models.CharField(max_length=50, default="0|0|0|0|0")
#     blogaddress = models.CharField(max_length=500, default="")
#     cfrate = models.CharField(max_length=500, default="0|0|0")  # 分数|最近一个月场数|上下分
#
#     objects = models.Manager()
#
#     def __str__(self):
#         return self.username
#
#
class DailyTable(models.Model):
    username = models.CharField(max_length=50)
    account = models.IntegerField(default=0)
    collecttime = models.DateField(auto_now=True)
    cfrate = models.IntegerField(default=0)  # 分数

    objects = models.Manager()

    def __str__(self):
        return self.username

#
# class TeamBoard(models.Model):
#     teammember = models.CharField(max_length=100)
#     score = models.IntegerField(default=1500)
#     collecttime = models.DateField(auto_now=True)
#
#     objects = models.Manager()
#
#     def __str__(self):
#         return self.teammember
#
#
# class DailyContestBoard(models.Model):
#     contestdate = models.DateField(auto_now=True)
#     teammember = models.CharField(max_length=100)
#     problemcount = models.IntegerField(default=0)
#     wronglist = models.CharField(max_length=1000)  # A|B|C|F
#     wrongtime = models.CharField(max_length=1000)  # 0|0|1|0  没AC必为0
#     aclist = models.CharField(max_length=1000)  # A|B|C|F
#     actime = models.CharField(max_length=1000)  # 00:10:50|0|0|0  没AC必为0
#
#     objects = models.Manager()
#
#     def __str__(self):
#         return self.teammember
