from django.db import models

# Create your models here.

class Department(models.Model):
    title = models.CharField(verbose_name='标题',max_length=20)


class UserInfo(models.Model):
    name = models.CharField(max_length=18,verbose_name='姓名')
    password = models.CharField(max_length=36,verbose_name='密码')
    age = models.IntegerField(verbose_name='年龄')
    account = models.DecimalField(verbose_name='工资',max_digits=10,decimal_places=2,default=0)  #长度为8，精度为2
    create_time = models.DateTimeField(verbose_name='入职时间')

    depart = models.ForeignKey(Department,to_field='id',on_delete=models.CASCADE,)

    gender_choices = (
        (1,"男"),
        (2,"女"),
    )
    gender = models.SmallIntegerField(verbose_name='性别',choices=gender_choices)
