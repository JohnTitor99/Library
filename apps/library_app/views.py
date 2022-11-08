from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from ..base.models import Library, Wish, Finished

# Create your views here.

class LibraryOpen(generic.ListView):
    model = Library
    context_object_name = 'libraries'
    template_name = 'library_app/library_open.html'

    def post(self, request, *args, **kwargs):
        if 'wish-delete' in self.request.POST:
            wish_id = self.request.POST.get('wish_id')
            wish = Wish.objects.get(id=wish_id)
            wish.delete()

        elif 'move-to-finished' in self.request.POST:
            wish_id = self.request.POST.get('wish_id')
            wish = Wish.objects.get(id=wish_id)
            Finished.objects.create(user=self.request.user, library=wish.library, name=wish.name)
            wish.delete()

        elif 'finished-delete' in self.request.POST:
            finished_id = self.request.POST.get('finished_id')
            finished = Finished.objects.get(id=finished_id)
            finished.delete()

        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['libraries'] = context['libraries'].filter(user=self.request.user)
        context['wish_list'] = Wish.objects.filter(user=self.request.user)
        context['wish_list'] = context['wish_list'].filter(library__name=self.kwargs.get('lib_name'))
        context['finished_list'] = Finished.objects.filter(user=self.request.user)
        context['finished_list'] = context['finished_list'].filter(library__name=self.kwargs.get('lib_name'))
        context['lib_name'] = self.kwargs.get('lib_name')
        return context


class LibraryCreate(generic.CreateView):
    model = Library
    fields = ['name']
    template_name = 'library_app/library_create.html'
    success_url = reverse_lazy('libraries')

    # change form fields attributes
    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form = super().get_form(form_class)
        form.fields['name'].widget.attrs = {'placeholder': 'Name'} # add attributes to a field
        form.fields['name'].label = "" # change the label
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(LibraryCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['libraries'] = Library.objects.filter(user=self.request.user)
        return context


class LibraryDelete(generic.DeleteView):
    model = Library
    context_object_name = 'library'
    template_name = 'library_app/library_confirm_delete.html'
    success_url = reverse_lazy('libraries')

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class LibraryUpdate(generic.UpdateView):
    model = Library
    fields = ['name']
    template_name = 'library_app/library_update.html'
    success_url = reverse_lazy('libraries')
        
    # change form fields attributes
    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form = super().get_form(form_class)
        form.fields['name'].label = "" # change the label
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['libraries'] = self.model.objects.filter(user=self.request.user)
        context['lib_update'] = self.kwargs.get('pk') # id of updating library
        return context