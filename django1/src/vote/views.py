from django.shortcuts import render, get_object_or_404
from .models import *
from django.urls.base import reverse
from django.http.response import HttpResponseRedirect
from .forms import *
from _datetime import datetime
from django.contrib.auth.decorators import login_required
import os
#질문 리스트(index)
#질문 선택시 답변 항목제공(detail)
#웹 클라이언트가 선택한 답변항목의 투표수를 늘리는 처리(vote)
#웹 클라이언트가 선택한 질문의 답변 투표결과(result)
def index(request):
    qlist = Question.objects.all()
    return render(request, 'vote/index.html', {'objs':qlist})
def detail(request, q_id):
    q = get_object_or_404(Question, id=q_id)
    c_list = q.choice_set.all()
    return render(request, 'vote/detail.html', {'q':q, 'clist':c_list})
def vote(request):
    if request.method == "POST":
        c_id = request.POST.get('a')
        c = get_object_or_404(Choice, id=c_id)
        c.votes +=1
        c.save()
        return HttpResponseRedirect( reverse('vote:result', args=(c.q.id,)))
def result(request, q_id):
    q = get_object_or_404(Question, id=q_id)
    return render(request, 'vote/result.html', {'q':q})

@login_required
def qregister(request):
    if request.method == "GET":
        f = QuestionForm()
        return render(request, 'vote/qregister.html', {'f':f})
    elif request.method == "POST":
        f = QuestionForm(request.POST)
        if f.is_valid():
            print('cleaned_data["name"]', f.cleaned_data['name'])
            q = f.save(commit=False)
            q.date = datetime.now()
            print('데이터베이스에 저장되기 전 Question객체의 id값', q.id)
            q.save()
            print('데이터베이스에 저장된 후 id값', q.id)
            return HttpResponseRedirect(reverse('vote:detail', args=(q.id,)))
def qupdate(request, q_id):
    q = get_object_or_404(Question, id=q_id)
    if request.method == "GET":
        f = QuestionForm(instance = q)
        return render(request, 'vote/qregister.html', {'f':f})
    elif request.method == "POST":
        f = QuestionForm(request.POST, instance = q)
        if f.is_valid():
            qu = f.save()
            print('사용자 요청으로 찾으니 객체', q)
            print('값이 수정된 객체', qu)
            return HttpResponseRedirect(reverse('vote:detail', args=(q.id,)))
def qdelete(request, q_id):
    q = get_object_or_404(Question, id=q_id)
    print('데이터 베이스에 삭제되기전 id변수', q.id)
    q.delete()
    print('데이터 베이스에 삭제된 후 id변수', q.id)
    return HttpResponseRedirect(reverse('vote:index'))
def cregister(request):
    if request.method == "GET":
        f = ChoiceForm()
        return render(request, 'vote/cform.html', {'i':f.as_table()})
    elif request.method == "POST":
        f = ChoiceForm(request.POST)
        if f.is_valid():
            c = f.save()
            return HttpResponseRedirect(reverse('vote:detail', args=(c.q.id,)))
        else:
            return render(request, 'vote/cform.html', {'i':f.as_table(), 'error':'잘못된 임력입니다'})
def cupdate(request, c_id):
    c = get_object_or_404(Choice, id=c_id)
    if request.method == "GET":
        f = ChoiceForm(instance = c)
        return render(request, 'vote/cform.html', {'i':f.as_table()})
    elif request.method == "POST":
        f = ChoiceForm(request.POST, instance = c)
        if f.is_valid():
            f.save()
            return HttpResponseRedirect(reverse('vote:detail', args=(c.q.id,)))
def cdelete(request, c_id):
    c = get_object_or_404(Choice, id=c_id)
    c.delete()
    return HttpResponseRedirect(reverse('vote:detail', args=(c.q.id,)))