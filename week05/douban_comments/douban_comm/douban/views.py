from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.views import View

from .models import Douban
from .forms import DoubanForm
# from django.shortcuts import render
# from .models import Student

# Create your views here.
# def index(request):
#     # words = 'World!'
#     students = Student.objects.all()
#     return render(request, 'index.html', context={'students': students})

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