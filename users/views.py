from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from core.utils import get_url
import requests


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        keyword = self.request.query_params.get('search')
        if keyword is not None:
            queryset = get_user_model().objects.search_in_fields(keyword)
        else:
            queryset = self.queryset
        return queryset


class UserListView(ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    renderer_classes = (TemplateHTMLRenderer, )
    template_name = 'users/list.html'


class ProfileList(ListView):
    template_name = 'users/list.html'
    model = get_user_model()

    def get_context_data(self, **kwargs):
        base_url = get_url(self.request)
        url = '{}/users-api/'.format(base_url)
        users_serialized = requests.get(url, params=self.request.GET).json()
        context = super().get_context_data(**kwargs)
        context['object_list'] = users_serialized['results']
        return context


class UserCreate(CreateView):
    template_name = 'users/form.html'
    model = get_user_model()
    fields = ('first_name', 'last_name', 'email', 'phone', 'image_profile')


class UserDetail(DetailView):
    template_name = 'users/detail.html'
    model = get_user_model()


class UserEdit(UpdateView):
    template_name = 'users/form.html'
    model = get_user_model()
    fields = ('first_name', 'last_name', 'email', 'phone', 'image_profile')


class UserDelete(DeleteView):
    model = get_user_model()
    success_url = reverse_lazy('user-list')
