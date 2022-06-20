from django.db import models


# Create your models here.

class Department(models.Model):
    title = models.CharField(verbose_name='标题', max_length=20)

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    name = models.CharField(max_length=18, verbose_name='姓名')
    password = models.CharField(max_length=36, verbose_name='密码')
    age = models.IntegerField(verbose_name='年龄')
    account = models.DecimalField(verbose_name='工资', max_digits=10, decimal_places=2, default=0)  # 长度为8，精度为2
    create_time = models.DateField(verbose_name='入职时间')

    depart = models.ForeignKey(verbose_name='部门', to=Department, to_field='id', on_delete=models.CASCADE, )

    gender_choices = (
        (1, "男"),
        (2, "女"),
    )
    gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choices)


class PrettyNum(models.Model):
    mobile = models.CharField(verbose_name='手机号', max_length=11)
    price = models.IntegerField(verbose_name='价格', default=0)
    level_choices = (
        (1, '普通'),
        (2, '卓越'),
        (3, '极品')
    )
    level = models.SmallIntegerField(verbose_name='等级', choices=level_choices, default=1)
    status_choice = (
        (1, '已使用'),
        (2, '未使用'),
    )
    status = models.SmallIntegerField(verbose_name='状态', choices=status_choice, default=2)


class Admin(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)
    def __str__(self):
        return self.username

class Task(models.Model):
    """ 任务 """
    level_choices = (
        (1, "紧急"),
        (2, "重要"),
        (3, "临时"),
    )
    level = models.SmallIntegerField(verbose_name="级别", choices=level_choices, default=1)
    title = models.CharField(verbose_name="标题", max_length=64)
    detail = models.TextField(verbose_name="详细信息")
    user = models.ForeignKey(verbose_name="负责人", to="Admin", on_delete=models.CASCADE)
