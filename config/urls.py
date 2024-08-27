from django.urls import path, include

urlpatterns = [
    path('news/' , include('blog_app.urls')),
]
from django.urls import path,include
from django.views.generic import TemplateView
from django.shortcuts import render
class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name)


urlpatterns = [
    path('' , HomeView.as_view(), name='home'),
    path('news/', include('blog_app.urls'))
  
]
