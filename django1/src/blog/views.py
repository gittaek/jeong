from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from blog.models import Post, PostFile, PostImage
from blog.forms import PostForm
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

#제네릭뷰: 장고에서 제공하는 여러가지 뷰 기능을 구현한 클래스
#ListView: 특정 모델의 객체 목록을 다루는 기능이 구현
#DetailView: 특정 모델클래스의 객체 1개를 다루는 기능이 구현
#FormView: 특정 폼클래스를 다루는 기능이 구현

#index: 글목록이 뜨는 메인 페이지
class Index(ListView):
    template_name = 'blog/index.html'
    model = Post
    context_object_name = 'list'
    pageinate_by = 5

#detail: 글 상세보기 페이지
class Detail(DetailView):
    template_name = 'blog/detail.html'
    model = Post
    context_object_name = 'obj'

#posting: 글쓰기 페이지
class Posting(LoginRequiredMixin, FormView):
    template_name = 'blog/posting.html'
    form_class = PostForm
    context_object_name = 'f'
    
    def form_valid(self, form):
        p = form.save(commit=False)
        p.author = self.request.user
        p.save()
        for f in self.request.FILES.getlist('files'):
            pf = PostFile()
            pf.file = f
            pf.post = p
            pf.save()
        for i in self.request.FILES.getlist('images'):
            pi = PostImage()
            pi.post = p
            pi.image = i
            pi.save()
        return HttpResponseRedirect(reverse('blog:detail', args=(p.id,)))