#하위 URLConf
#app_name: 하위 URLConf 파일의 등록된 URL들의 그룹명
#urlpatterns: URL과 뷰함수를 이그트형태로 등록하는 변수
from django.urls import path
from .views import *

app_name = 'cl'
urlpatterns = [
    path('signup/', signup, name= 'signup'),
    path('signin/', signin, name= 'signin'),
    path('signout/', signout, name= 'signout'),
]