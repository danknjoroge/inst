from . import views
from django.urls import path, re_path, include

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]