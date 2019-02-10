from django.db import models

'''
질문
질문제목 생성일

답변
어떤질문에 연결되있는지 답변내용 투표수
'''
class Question(models.Model):
    name = models.CharField('질문', max_length=100)
    date = models.DateTimeField('생성일')
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-date']
class Choice(models.Model):
    q = models.ForeignKey(Question, on_delete=models.CASCADE)
    name = models.CharField('항목', max_length=50)
    votes = models.IntegerField('투표수', default=0)
    def __str__(self):
        return self.q.name+'/'+self.name