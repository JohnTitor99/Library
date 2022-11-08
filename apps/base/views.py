from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import views
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Library


class LoginPage(views.LoginView):
    template_name = 'base/login_page.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('libraries')


class LibrariesList(LoginRequiredMixin, generic.ListView):
    model = Library
    context_object_name = 'libraries'
    template_name = 'base/main_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['libraries'] = context['libraries'].filter(user=self.request.user)
        return context
