from django.views.generic import TemplateView , DetailView
from django.shortcuts import render, redirect, get_object_or_404
from .models import News
from.forms import NewsForm

class NewsListView(TemplateView):
    template_name = 'news/list.html'

    def get(self, request):
        context = {
            'object': News.objects.all()
        }
        return render(request, self.template_name , context)

class NewsCreateView(TemplateView):
   template_name = 'news/form.html'

   def get(self, request):
      return render(request, self.template_name, {'form':NewsForm()})

   def post(self, request):
      form = NewsForm(request.POST)
      if form.is_valid(): 
          object = form.save()
          return redirect('news_detail' , object.id)
      return render(request , 'news/form.html',{'form' : form})
       
class NewsDetailView(DetailView):
   template_name = 'news/detail.html'

   def get(self, request, pk):
      context={ 'object': get_object_or_404(News, id = pk) }

      return render(request, self.template_name, context)
   
class NewsUpdateView(TemplateView):
   template_name = 'news/form.html'

   def get(self, request ,pk):
      object = get_object_or_404(News, pk = pk)
      context = {
         'form' : NewsForm(instance=object)
      }
      return render(request,self.template_name , context)
   def post(self, request, pk):
      object = get_object_or_404(News, pk = pk)
      form = NewsForm(request.POST, instance=object)
      if form.is_valid(): 
          object = form.save()
          return redirect('news_detail', object.id)
      return render(request , 'news/form.html',{'form' : form})
   
class NewsDeleteView(TemplateView):
   def get(self, request, pk):
      news = get_object_or_404(News , pk = pk)
      news.delete()
      return redirect('news_list')