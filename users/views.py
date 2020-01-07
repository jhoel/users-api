
import requests

from core.utils import get_url
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import TemplateView
from django.views.generic import UpdateView
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        keyword = self.request.query_params.get('search')
        queryset = get_user_model().objects.search_in_fields(keyword)
        return queryset


class UserListView(ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    renderer_classes = (TemplateHTMLRenderer, )
    template_name = 'users/list.html'


class ProfileList(TemplateView):
    template_name = 'users/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        url = '{}/users-api/'.format(get_url(self.request))
        user_api_response = requests.get(url, params=self.request.GET)
        users_serialized = {}
        if user_api_response:
            users_serialized = user_api_response.json()['results']
        else:
            context['api_error'] = True

        context['object_list'] = users_serialized
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
