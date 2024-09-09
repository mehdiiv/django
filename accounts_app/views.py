from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from blog_app.models import News
from .forms import UserLogin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth import views as auth_views

class RequiredLoginView(LoginRequiredMixin, TemplateView):
   pass

class LoginView(TemplateView):
   template_name = 'login.html'
   
   def get(self, request):
      context = {
         'login_form': UserLogin()        
      }
      return render(request, self.template_name, context)
   
   def post(self, request):
      form = UserLogin(request.POST)
      if form.is_valid():
         username= form.cleaned_data['username']
         password = form.cleaned_data['password']
         user = authenticate(request, username = username, password = password)
         if user != None:
            login(request, user)
            return redirect('home')
         else:
            form.add_error('username', 'invlid username or password')
            return render(request, self.template_name, { 'login_form' : form })

class LogoutView(TemplateView):
   def get(self, request):
      logout(request)
      return redirect('login')

class SendEmailView(RequiredLoginView):
   def get(self ,request, pk):
      news = get_object_or_404(News, pk = pk)
      subject = 'hello, {0}'.format(news.writer)
      context = {'news.writer': news.writer}
      body = render_to_string('mails/sample.html', context)
      email = EmailMultiAlternatives(subject, "",'', [news.email])
      email.attach_alternative(body, "text/html")
      email.send()
      return redirect('news_detail', news.id) 
   
class ResetPasswordView(SuccessMessageMixin, auth_views.PasswordResetView):
    template_name = 'registration/password_reset_form.html'

class ResetPasswordDoneView(auth_views.PasswordResetDoneView):
   template_name = 'registration/password_reset_done.html'