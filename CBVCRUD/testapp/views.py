from django.shortcuts import render,redirect
from .models import Books
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy

class list(ListView):
    model=Books
    template_name = 'testapp/list.html'
    context_object_name = 'book'

class insert(CreateView):
    model = Books
    template_name = 'testapp/insert.html'
    fields = ('title','author','pages','price')

class update(UpdateView):
    model = Books
    fields = '__all__'
    template_name = 'testapp/update.html'

class delete(DeleteView):
    model = Books
    success_url = reverse_lazy('detail')
