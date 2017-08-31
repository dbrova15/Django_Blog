"""Spalah_Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views   /media/yaponskij_sad.jpg
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static

from Spalah_Django import settings
from . import views

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^japanese_garden$', views.japanese_garden, name="japanese_garden"),
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^login/$', views.log_in, name='login'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^upload_file/$', views.upload_file, name='upload_file'),
    url(r'^news/', views.news_list, name='news_list'),
    url(r'^logout/$', views.logout_view, name='logout'),
    #url(r'^post_del/$', views.post_del, name='post_del'),
    url(r'^signup/$', views.signup, name='signup'),
    #url(r'^delete_post/(?P<id>\d+)/', 'delete_post', name="delete_post"),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
