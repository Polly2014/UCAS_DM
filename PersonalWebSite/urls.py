"""PersonalWebSite URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from UCAS_DM import views as ucas_dm_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', ucas_dm_views.dm_index, name='index'),
    # url(r'^wx/', include('WeChatSite.urls', namespace='WeChatSite')),
    url(r'^ucas_dm/', include('UCAS_DM.urls', namespace='UCAS_DM')),
    # url(r'^freecandy/', include('FreeCandy.urls', namespace='FreeCandy')),
]
