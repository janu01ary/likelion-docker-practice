from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import imgapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', imgapp.views.home, name='home'),
    path('detail/<int:id>', imgapp.views.detail, name='detail'),
    path('create', imgapp.views.create, name='create'),
    path('update/<int:id>', imgapp.views.update, name='update'),
    path('delete/<int:id>', imgapp.views.delete, name='delete'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)