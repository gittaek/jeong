#form: html의 <form>태그에 들어가는 <input>태그들을 관리하는 클래스/기능
#모델클래스에 저장된 변수들에 맞춰 자동설정도 할수있고, 커스텀입력공간(비밀번호 확인)도 생성할수있음

#class 클래스명(ModelForm 또는 Form)
#ModelForm: 모델클래스를 기반으로 입력양식을 자동 생성할때 상속받는 클래스
#Form: 커스텀 입력양식을 생성할때 상속받는 클래스
#ModelForm을 상속받았을 때도 커스텀 입력양식을 생성할 수 있음

#폼 클래스의 객체를 함수를 통해서 html문서의 코드로 변환할 수 있음(<p>,<table>,<li>)
#예시) 폼클래스객체.as_p() -> 해당 폼 객체에 저장된 입력공간들을 <input>태그로 변환하고, 개별적으로 <p>태그로 묶은 문자열을 반환
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

class SignupForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password_check'].label = '비밀번호 확인'
    password_check = forms.CharField(max_length=200, widget=forms.PasswordInput())
    field_order = ['username', 'password', 'password_check', 'last_name', 'first_name', 'email']
    class Meta:
        model = User
        widgets={'password':forms.PasswordInput()}
        fields = ['username', 'password', 'last_name', 'first_name', 'email']
class SigninForm(ModelForm):
    class Meta:
        model = User
        fields=['username', 'password']