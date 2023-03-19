from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import login
from django.contrib.auth.models import User

from .models import Library


class LoginPage(views.LoginView):
    template_name = 'base/login_page.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('libraries')


class RegisterPage(generic.FormView):
    template_name = 'base/register_page.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('libraries')

    # remove UserCreationForm helptext
    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form = super().get_form(form_class)
        form.fields['username'].help_text = None
        form.fields['password1'].help_text = None
        form.fields['password2'].help_text = None
        return form

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)


class EditProfile(generic.UpdateView):
    model = User
    template_name = 'base/edit_profile.html'
    success_url = reverse_lazy('libraries')
    fields = ['username']

    def get_object(self):
        return self.request.user

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form = super().get_form(form_class)
        form.fields['username'].widget.attrs = {'class': 'userprofile-input-field'}
        form.fields['username'].help_text = None # change the label
        return form


class PasswordChange(views.PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('libraries')
    template_name = 'base/change_password.html'

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form = super().get_form(form_class)
        form.fields['old_password'].widget.attrs = {'class': 'userprofile-input-field'}
        form.fields['new_password1'].widget.attrs = {'class': 'userprofile-input-field'}
        form.fields['new_password2'].widget.attrs = {'class': 'userprofile-input-field'}
        form.fields['new_password1'].help_text = None
        return form


class LibrariesList(LoginRequiredMixin, generic.ListView):
    model = Library
    context_object_name = 'libraries'
    template_name = 'base/main_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['libraries'] = context['libraries'].filter(user=self.request.user)
        return context


class LibrarySearch(LoginRequiredMixin, generic.ListView):
    model = Library
    context_object_name = 'libraries'
    template_name = 'base/lib_search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['libraries'] = context['libraries'].filter(user=self.request.user)

        # search
        search_input = self.request.GET.get('q') or ''
        if search_input:
            context['libraries'] = context['libraries'].filter(name__icontains=search_input)
        context['search_input'] = search_input
        return context
