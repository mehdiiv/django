from django.views.generic import TemplateView , DetailView
from django.shortcuts import render, redirect, get_object_or_404
from .models import News
from.forms import NewsForm, UserLogin
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

class RequiredLoginView(LoginRequiredMixin, TemplateView):
   pass

class NewsListView(RequiredLoginView):
    template_name = 'news/list.html'

    def get(self, request):
        context = {
            'object': News.objects.filter(writer = request.user )
        }
        return render(request, self.template_name, context)

class NewsCreateView(RequiredLoginView):
   template_name = 'news/form.html'

   def get(self, request):
      return render(request, self.template_name, { 'form': NewsForm() })

   def post(self, request):
      form = NewsForm(request.POST)
      form.instance.writer = request.user
      if form.is_valid(): 
          object = form.save()
          return redirect('news_detail', object.id)
      return render(request, 'news/form.html', { 'form': form })
       
class NewsDetailView(RequiredLoginView):
   template_name = 'news/detail.html'

   def get(self, request, pk):
      
      id = get_object_or_404(News, id = pk)
      context = { 'object': id }

      return render(request, self.template_name, context)
   
class NewsUpdateView(RequiredLoginView):
   template_name = 'news/form.html'

   def get(self, request ,pk):
      object = get_object_or_404(News, pk = pk)
      context = {
         'form' : NewsForm(instance = object)
      }
      return render(request, self.template_name, context)
   def post(self, request, pk):
      object = get_object_or_404(News, pk = pk)
      form = NewsForm(request.POST, instance = object)
      if form.is_valid(): 
          object = form.save()
          return redirect('news_detail', object.id)
      return render(request, 'news/form.html', { 'form': form })
   
class NewsDeleteView(RequiredLoginView):
   def get(self, request, pk):
      news = get_object_or_404(News , pk = pk)
      news.delete()
      return redirect('news_list')

