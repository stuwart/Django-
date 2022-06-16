from django import forms
from app01 import models
from django.core.exceptions import ValidationError

class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ['name', 'password', 'age', 'account', 'create_time', 'depart', 'gender']
        # labels = {
        #     'name':'请输入姓名',
        #     'password':'请输入密码',
        #     'age':'请输入年龄',
        # }
        error_messages = {
            '__all__': {'required': '请输入内容！',
                        'invalid': '内容有误，请检查！'}
        }

        # widgets = {
        #     'name' : forms.TextInput(attrs={'class':'form-control'}),
        #     'password':forms.PasswordInput(attrs={'class':'form-control'}),
        #     'age'
        # }


        def __init__(self, *args, **kwargs):
            super.__init__(*args, **kwargs)
            #循环找到所有插件 ，赋予样式
            for name, field in self.fields.items():
                print(name, field)
                field.widget.attrs = {'class': 'form-control','placeholder':field.label}
