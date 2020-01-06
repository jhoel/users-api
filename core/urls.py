"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework import routers
from users.views import UserViewSet, ProfileList, UserCreate, UserDetail, UserEdit, UserDelete, UserListView

router = routers.DefaultRouter()
router.register('users-api', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('index/', ProfileList.as_view()),


    path('users/', ProfileList.as_view(), name='user-list'),
    path('usersss/', UserListView.as_view(), name='user-list-api'),
    path('users/create/', UserCreate.as_view(), name='user-create'),
    path(r'users/<int:pk>', UserDetail.as_view(), name='user-detail'),
    path(r'users/<int:pk>/edit', UserEdit.as_view(), name='user-edit'),
    path(r'users/<int:pk>/delete', UserDelete.as_view(), name='user-delete'),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
