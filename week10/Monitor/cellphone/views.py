import urllib.parse
from .models import Cellphone
from django.db.models import Avg
from django.shortcuts import render,redirect
from .form import RequestForm

# Create your views here.
# def book(request):
    # n = Cellphone.objects.all()
    # return render(request,'test.html',locals())

def estimate_url(request):
    form = RequestForm()
    shorts = Cellphone.objects.all()
    # 评论数量
    counter = Cellphone.objects.all().count()
    # 平均星级
    # star_avg = 3.4
    star_avg = f" {Cellphone.objects.aggregate(Avg('n_star'))['n_star__avg']:0.1f} "
    # 情感倾向
    # sent_avg = 0.78
    sent_avg = f" {Cellphone.objects.aggregate(Avg('sentiment'))['sentiment__avg']:0.2f} "
    
    # 正向数量
    queryset = Cellphone.objects.values('sentiment')
    condtions = {'sentiment__gte': 0.5}
    plus = queryset.filter(**condtions).count()
    
    # 负向数量
    queryset = Cellphone.objects.values('sentiment')
    condtions = {'sentiment__lt': 0.5}
    minus = queryset.filter(**condtions).count()
    return render(request,'result1.html',locals())

# action="/request_url" method="post"
def request_url(request,name):
    if request.method == 'POST':
        try:
            condtions = {}
            form = RequestForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                if cd['text']:
                    print('-'*40)
                    cd['text']= urllib.parse.unquote(cd['text'])
                    # print(cd['text'])
                    condtions['estimate__contains'] = cd['text']
                if cd['start_time']:
                    # print('='*40)
                    # print(cd['start_time'])
                    condtions['date__gte'] = cd['start_time']
                if cd['last_time']:
                    # print(cd['last_time'])
                    condtions['date__lte'] = cd['last_time']
                shorts = Cellphone.objects.filter(**condtions)
                counter = Cellphone.objects.filter(**condtions).count()
                # 平均星级
                star_avg = f"{Cellphone.objects.filter(**condtions).aggregate(Avg('n_star'))['n_star__avg']:0.1f}"
                # 情感倾向
                sent_avg = f"{Cellphone.objects.filter(**condtions).aggregate(Avg('sentiment'))['sentiment__avg']:0.2f}"
                # 正向数量
                queryset = Cellphone.objects.filter(**condtions).values('sentiment')
                condtions = {'sentiment__gte': 0.5}
                plus = queryset.filter(**condtions).count()
                # 负向数量
                queryset = Cellphone.objects.filter(**condtions).values('sentiment')
                condtions = {'sentiment__lt': 0.5}
                minus = queryset.filter(**condtions).count()
                return render(request, 'result1.html',locals())
        except Exception:
            form = RequestForm()
            point = '没有搜索到需要的信息...'
            return render(request, 'result1.html',locals())
        
    if request.method == "GET":
        form = RequestForm()
        return render(request, 'result1.html',locals())
