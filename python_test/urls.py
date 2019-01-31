"""python_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from clients.views import NewClientView, UpdateClientView, ClientListView, ClientSearchView, search

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', TemplateView.as_view(template_name="home.html"))
    url('^$', TemplateView.as_view(template_name='base.html'), name='home'),

    url(r'^create/$', NewClientView.as_view(), name='create'),
    url(r'^client/(?P<pk>\d+)/update/$', UpdateClientView.as_view(), name='update'),
    #url(r'^clients/$', ClientListView.as_view(), name='list'),
    url(r'^search/$', search, name='search'),
]
