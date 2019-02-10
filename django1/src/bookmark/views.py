from django.shortcuts import render
from .models import Bookmark

def index(request):
    return render(request, 'bookmark/index.html', {'a':"hello", 'b':[1,2,3,4,5]})
def booklist(request):
    #모델클래스.objects.get(): 데이터베이스에 해당 모델클래스로 저장된 객체중 특정조건을 만족하는 객체 한개를 추출하는 함수
    #모델클래스.objects.all(): 데이터베이스에 해당 모델클래스로 저장된 모든 객체를 추출
    #모델클래스.objects.filter(): 데이터베이스에 특정조건을 만족하는 모든객체를 리스트 형태로 추출
    #모델클래스.objects.exclude(): 데이터베이스에 특정조건을 만족하지않는 모든객체를 리스트 형태로 추출
    list = Bookmark.objects.all()
    return render(request, 'bookmark/booklist.html', {'objs':list})
def getbook(request, bookid):
    #객체 한개를 추출할 때, 객체별로 저장된 고유한 id값을 이용해 추출함
    #어떤 id값을 가진 객체를 요청했는지 알아야된
    #=>뷰함수의 매개변수를 늘림, <form>로 넘어온 데이터 처리\
    obj = Bookmark.objects.get(id=bookid)
    print(obj)
    return render(request, 'bookmark/getbook.html', {'book':obj})