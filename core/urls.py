from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from rest_framework import routers
from users.views import ProfileList
from users.views import UserCreate
from users.views import UserDelete
from users.views import UserDetail
from users.views import UserEdit
from users.views import UserListView
from users.views import UserViewSet

router = routers.DefaultRouter()
router.register('users-api', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('users/', ProfileList.as_view(), name='user-list'),
    path('users/create/', UserCreate.as_view(), name='user-create'),
    path('users/<int:pk>', UserDetail.as_view(), name='user-detail'),
    path('users/<int:pk>/edit', UserEdit.as_view(), name='user-edit'),
    path('users/<int:pk>/delete', UserDelete.as_view(), name='user-delete'),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
