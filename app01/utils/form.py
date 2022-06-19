from django import forms
from app01 import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from app01.utils.bootstrap import *
from app01.utils.encrypt import *


class UserModelForm(BootStrapModelForm):
    class Meta:
        model = models.UserInfo
        fields = ['name', 'password', 'age', 'account', 'create_time', 'depart', 'gender']
        error_messages = {
            '__all__': {'required': '请输入内容！',
                        'invalid': '内容有误，请检查！'}
        }
        # labels = {
        #     'name':'请输入姓名',
        #     'password':'请输入密码',
        #     'age':'请输入年龄',
        # }

        widgets = {
            #     'name' : forms.TextInput(attrs={'class':'form-control'}),
            #  'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            #     'age'
        }


class PrettyModelForm(BootStrapModelForm):
    # 验证方式1：
    mobile = forms.CharField(
        label='手机号',
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误'), ],
    )

    class Meta:
        model = models.PrettyNum
        # fields = ['mobile', 'price', 'level', 'status']
        fields = '__all__'
        # exclude = ['']

    # 验证方式2：
    def clean_mobile(self):
        txt_mobile = self.cleaned_data['mobile']
        exists = models.PrettyNum.objects.filter(mobile=txt_mobile).exists()
        if exists:
            return ValidationError('该手机号已存在')
        return txt_mobile


class AdminModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(
        label='确认密码',
        widget=forms.PasswordInput(render_value=True),
    )

    class Meta:
        model = models.Admin
        fields = '__all__'
        widgets = {
            'passowrd': forms.PasswordInput(render_value=True),
        }

    def clean_passowrd(self):
        pwd = self.cleaned_data['passowrd']
        return md5(pwd)

    def clean_confirm_password(self):
        pwd = self.cleaned_data['passowrd']
        confirm = md5(self.cleaned_data['confirm_password'])
        if pwd != confirm:
            raise ValidationError('两次输入的密码不一致！')
        return confirm
