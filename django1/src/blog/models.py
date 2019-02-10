from django.db import models
from django.contrib.auth.models import User
#카테고리
    #카테고리 이름
class PostType(models.Model):
    name = models.CharField('카테고리', max_length=20)
    def __str__(self):
        return self.name
    
#글 정보
    #제목, 글쓴이-외래키, 글내용, 작성일, 카테고리-외래키
class Post(models.Model):
    category = models.ForeignKey(PostType, on_delete=models.CASCADE)
    headline = models.CharField('제목', max_length=200)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    content = models.TextField('내용', null=True, blank=True)
    pub_date =models.DateTimeField('작성일', auto_now_add=True)
    class Meta:
        ordering = ['-pub_date']
#글에 포함된 이미지 정보
    #글-외래키, 이미지파일(ImageFiled, Pillow(파이썬에서 사용되는 대표적인 이미지 처리모듈)모듈 필요)
class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField('이미지파일', upload_to='images/%Y/%m/%d')
    
#글에 포함된 첨부파일 정보
    #글-외래키, 파일
class PostFile(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file = models.FileField('첨부파일', upload_to='files/%Y/%m/%d')
    