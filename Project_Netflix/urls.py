"""Project_Netflix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
# MEDIA AYARLARI(DINAMIK DOSYA EKLEMEK ICIN YAPILAN IMPORTLAR)
from django.conf import settings
from django.conf.urls.static import static
# views.py dosyasında sayfaları görüntülemek için yazılan fonksiyonları burada kullanamk için yapılması gereken import.
from myApp.views import *
from myUser.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('Netflix/<bid>/',indexBrowse,name='indexBrowse'),
    path('Login/',loginUser,name='loginUser'), #giriş yap
    path('Logout/',logoutUser,name='logoutUser'), 
    path('Register/',registerUser,name='registerUser'), #kayıt ol
    path('Profiller/',browse,name='browse'), 
    path('Hesap/<hid>/',hesap,name='hesap'), 
    path('ProfilDel/<pid>/',browseDel,name='browseDel'), 
    path('Netflix/<categoryId>/',index2,name='index2'),
    path('',include('movies.urls'))

] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
# media ayarları urlpatterns listesinin sonuna + koyularak yazılır.
