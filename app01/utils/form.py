from django import forms
from app01 import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class UserModelForm(forms.ModelForm):
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
             'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            #     'age'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环找到所有插件 ，赋予样式
        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}


class PrettyModelForm(forms.ModelForm):
    mobile = forms.CharField(
        label='手机号',
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误'), ],
    )

    class Meta:
        model = models.PrettyNum
        # fields = ['mobile', 'price', 'level', 'status']
        fields = '__all__'
        # exclude = ['']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环找到所有插件 ，赋予样式
        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}

    def clean_mobile(self):
        txt_mobile = self.cleaned_data['mobile']
        exists = models.PrettyNum.objects.filter(mobile=txt_mobile).exists()
        if exists:
            return ValidationError('该手机号已存在')
        return txt_mobile
