from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from ..base.models import Library, Wish, Finished


class WishCreate(generic.CreateView):
    model = Wish
    fields = ['name']
    template_name = 'wish_list_app/wish_create.html'

    # it needs here a method, not an atribute, because of kwargs transition
    def get_success_url(self, **kwargs):
        return reverse_lazy('library_open', kwargs={'lib_name': self.kwargs.get('lib_name')})

    # change form fields attributes
    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = super().get_form(form_class)
        form.fields['name'].widget.attrs = {'placeholder': 'Name', 'class': 'create-form-input'} # add attributes to a field
        form.fields['name'].label = "" # change the label
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.library = Library.objects.filter(user=self.request.user).get(name=self.kwargs.get('lib_name'))
        return super(WishCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['libraries'] = Library.objects.filter(user=self.request.user)
        context['wish_list'] = Wish.objects.filter(user=self.request.user)
        context['wish_list'] = context['wish_list'].filter(library__name=self.kwargs.get('lib_name'))
        context['finished_list'] = Finished.objects.filter(user=self.request.user)
        context['finished_list'] = context['finished_list'].filter(library__name=self.kwargs.get('lib_name'))
        context['lib_name'] = self.kwargs.get('lib_name')
        return context


# class WishDelete(generic.DeleteView):
#     model = Wish
#     context_object_name = 'wish'
#     template_name = 'wish_list_app/wish_confirm_delete.html'

#     # it needs here a method, not an atribute, because of kwargs transition
#     def get_success_url(self, **kwargs):
#         return reverse_lazy('library_open', kwargs={'lib_name': self.kwargs.get('lib_name')})

#     def get_query_set(self):
#         return self.model.objects.filter(user=self.request.user)

#     # passing a lib_name is for "go back" button
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['lib_name'] = self.kwargs.get('lib_name')
#         return context


class WishUpdate(generic.UpdateView):
    model = Wish
    fields = ['name']
    template_name = 'wish_list_app/wish_update.html'
    
    # it needs here a method, not an attribute, because of kwargs transition
    def get_success_url(self, **kwargs):
        return reverse_lazy('library_open', kwargs={'lib_name': self.kwargs.get('lib_name')})

    # change form fields attributes
    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form = super().get_form(form_class)
        form.fields['name'].widget.attrs = {'class': 'update-form-input'} # add attributes to a field
        form.fields['name'].label = "" # change the label
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['libraries'] = Library.objects.filter(user=self.request.user)
        context['wish_list'] = Wish.objects.filter(user=self.request.user)
        context['wish_list'] = context['wish_list'].filter(library__name=self.kwargs.get('lib_name'))
        context['finished_list'] = Finished.objects.filter(user=self.request.user)
        context['finished_list'] = context['finished_list'].filter(library__name=self.kwargs.get('lib_name'))
        context['lib_name'] = self.kwargs.get('lib_name')
        context['wish_update'] = self.kwargs.get('pk')
        return context
