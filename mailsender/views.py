from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import SpamServis, Client, Message


class SpamServisListView(ListView):
    model = SpamServis
    template_name = 'spamservis_list.html'


class SpamServisDetailView(DetailView):
    model = SpamServis
    template_name = 'spamservis_detail.html'


class ClientListView(ListView):
    model = Client
    template_name = 'client_list.html'


class MessageListView(ListView):
    model = Message
    template_name = 'message_list.html'