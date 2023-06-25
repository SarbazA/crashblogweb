
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path , include

from core.views import frontpage ,about , robots_txt

urlpatterns = [
    path(' robots_txt', robots_txt,name=" robots_txt"),
    path('admin/', admin.site.urls),
    path('about/' , about , name='about'),
    path('', include('blog.urls')),
    path('', frontpage , name='frontpage'),
   
]
urlpatterns= urlpatterns+static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)