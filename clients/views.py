from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView, DetailView
from .models import models
from .models import Client, Vehicle, Comment
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class ClientListView(LoginRequiredMixin,ListView):
    model = Client
    template_name = 'client_list.html'

class ClientUpdateView(LoginRequiredMixin,UpdateView):
    model = Client
    fields = ('name', 'notes', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone', 'acct_number')
    template_name = 'client_edit.html'

class ClientDetailView(LoginRequiredMixin,DetailView):
    model = Client
    template_name = 'client_detail.html'
    login_url = 'login'

class ClientDeleteView(LoginRequiredMixin,DeleteView):
    model = Client
    template_name = 'client_delete.html'
    success_url = reverse_lazy('client_list')

class ClientCreateView(LoginRequiredMixin,CreateView):
    model = Client
    template_name = 'client_new.html'
    fields = ('name', 'notes', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone', 'acct_number')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CommentCreateView(LoginRequiredMixin,CreateView):
    model = Comment
    template_name = 'comment_new.html'
    fields = ('client', 'comment', 'author')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class VehicleUpdateView(LoginRequiredMixin,UpdateView):
    model = Vehicle
    fields = ('client', 'make', 'model', 'vin_number', 'date_of_purchase', 'author')
    template_name = 'vehicle_edit.html'

class VehicleDetailView(LoginRequiredMixin,DetailView):
    model = Vehicle
    template_name = 'vehicle_detail.html'
    login_url = 'login'
