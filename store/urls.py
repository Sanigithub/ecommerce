from django.urls import path
from .views import shop, signin, signup
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', shop, name='shop'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
