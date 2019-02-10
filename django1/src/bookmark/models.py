from django.db import models

#모댈 클래스 정의 시, models.Model클래스를 상속받아 모델클래스 정의
class Bookmark(models.Model):
    #클래스 변수를 생성해 해당 모델 클래스가 어떤 값들을 저장하는지 정의
    #클래스 변수 = models.XXXXFields 클래스의 객체를 저장하는 것으로 저장공간을 정의
    name = models.CharField(max_length=20)
    url = models.URLField()
    def __str__(self):
        return self.name