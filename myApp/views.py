from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from myUser.models import *
from myApp.models import *

# sayfaları görüntüleyebilmek için fonksiyonlarının yazılması gerekir.
# fonksiyonu yazılan sayfanın urls.py dosyasında path tanımlaması yapılır. 

def index(request):
    context={"title":"Anasayfa"}
    return render(request,'index.html',context)

@login_required(login_url='loginUser') #giriş yapmadan izin vermez
def indexBrowse(request,bid):
    context={"title":"Netflix"}
    profil = Profil.objects.get(id=bid)
    context.update({'profil':profil})
    
    return render(request,'browse-index.html',context)


