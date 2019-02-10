from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .forms import SigninForm, SignupForm
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse

#질문 리스트(index)
#질문 선택시 답변 항목제공(detail)
#웹 클라이언트가 선택한 답변항목의 투표수를 늘리는 처리(vote)
#웹 클라이언트가 선택한 질문의 답변 투표결과(result)
def signup(request):
    if request.method == "GET":
        f = SignupForm()
        return render(request, 'cl/signup.html', {'f':f})
    elif request.method == "POST":
        f = SignupForm(request.POST)
        if f.is_valid():
            if f.cleaned_data['password'] == f.cleaned_data['password_check']:
                new_user = User.objects.create_user(username=f.cleaned_data['username'], email=f.cleaned_data['email'], password=f.cleaned_data['password'])
                new_user.last_name = f.cleaned_data['last_name']
                new_user.first_name = f.cleaned_data['first_name']
                new_user.save()
                return HttpResponseRedirect(reverse('cl:signin'))
            else:
                return render(request, 'cl/signup.html', {'f':f, 'error':'비밀번호가 일치하지 않습니다.'})
        else:
            return render(request, 'cl/signup.html', {'f':f})
def signin(request):
    if request.method == "GET":
        return render(request, 'cl/signin.html', {'f':SigninForm()})
    elif request.method == "POST":
        f = SigninForm(request.POST)
        id = request.POST.get('username')
        pw = request.POST.get('password')
        u = authenticate(username=id, password=pw)
        if u:
            login(request, u)
            nexturl = request.POST.get('nexturl')
            if nexturl:
                return HttpResponseRedirect(nexturl)
            else:
                return HttpResponseRedirect(reverse('blog:index'))
        else:
            return render(request, 'cl/signin.html', {'f':f, 'error':'아이디나 비밀번호가 일치하지 않습니다.'})
def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('cl:signin'))