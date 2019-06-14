"""blogs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog import views

app_name = "blog"

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^index/', views.index,name='index'),
    url(r'^to_blog_page/(?P<article_id>[0-9]+)$', views.to_blog_page, name='to_blog_page'),
    url(r'^blog_delete/(?P<article_id>[0-9]+)$', views.blog_delete, name='blog_delete'),
    url(r'^edit_page/(?P<article_id>[0-9]+)$', views.edit_page, name='edit_page'),
    url(r'^edit_action$', views.edit_action, name='edit_action'),
    url(r'^create_page$', views.create_page, name='create_page'),
    url(r'^create_action$', views.create_action, name='create_action'),
    url(r'^export_excel', views.export_excel, name='export_excel'),

]
