from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from web_client import views

urlpatterns = [
    url(r'^$', views.Homepage.as_view(), name='homepage'),
]