"""to_do URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from tasks.views import home_view, delete_task, edit_task

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_view, name='home_view'),
    url(r'^delete/(?P<pk>[0-9]+)/$', delete_task, name='delete_task'),
    url(r'^edit/(?P<pk>[0-9]+)/$', edit_task, name='edit_task'),
]
