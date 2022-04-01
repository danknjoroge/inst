from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView


urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    path(r'home/', views.home, name='home'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'), 
    re_path(r'^login/$', LoginView.as_view(), {"next_page": '/'}),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)