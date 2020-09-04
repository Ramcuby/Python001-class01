from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render
from django.views import View

from .models import Douban
from .forms import DoubanForm
from .forms import LoginForm
from django.contrib.auth import authenticate, login

# from django.shortcuts import render

def login2(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # 读取表单的返回值
            cd = login_form.cleaned_data 
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                # 登陆用户
                login(request, user)  
                # context=['登录成功']
                # return render(request, 'index.html', {'form':'IndexView.as_view()'})
                return HttpResponseRedirect(reverse('index'))
            
            else:
                return HttpResponse('用户密码错误')
                # return HTTPRedirectHandler

    # GET
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, 'form2.html', {'form': login_form})

def index(request):
    words = 'World!'
    return render(request,'index.html',context={'words':words})

class IndexView(View):
    template_name = 'index.html'

    def get_context(self):
        doubans = Douban.get_all()
        context = {
            'doubans': doubans,
        }
        return context

    def get(self, request):
        context = self.get_context()
        form = DoubanForm()
        context.update({
            'form': form
        })
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = DoubanForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            douban = Douban()
            douban.author = cleaned_data['author']
            douban.star = cleaned_data['star']
            douban.comments = cleaned_data['comments']
            douban.save()
            return HttpResponseRedirect(reverse('index'))
        context = self.get_context()
        context.update({
            'form': form
        })
        return render(request, self.template_name, context=context)