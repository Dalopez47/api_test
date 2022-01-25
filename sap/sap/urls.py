from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from users.views import detailUser, newUser, editUser, deleteUser, listUsers
from webapp.views import welcome

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name='index'),
    path('list/', listUsers, name='list'),
    path('detail_user/<int:id>', detailUser),
    path('new_user/', newUser),
    path('edit_user/<int:id>', editUser),
    path('delete_user/<int:id>', deleteUser),

] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)