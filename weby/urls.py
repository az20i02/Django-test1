
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='weby/index/')),  # Redirect root to weby/index/
    path('admin/', admin.site.urls),
    path('weby/', include('main.urls')),
    path('items/', include('item.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('inbox/', include('conversation.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




#http://127.0.0.1:8000/main/index/