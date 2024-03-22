from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dealAdmin/', admin.site.urls),
    path('Home', include('home.urls',namespace='Home')),
    path('Blog', include('blog.urls',namespace='Blog')),
    path('Compitition', include('compitition.urls',namespace='Compitition')),
    path('Services', include('services.urls',namespace='services')),
    path('Contact_Us', include('contact_us.urls',namespace='contact')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)