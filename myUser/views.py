from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from myApp.models import *
from phone_field import PhoneField

# Create your views here.

def loginUser(request):
    context={"title":"GirişYap"}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('browse')
        else:
            messages.warning(request, 'Kulanıcı adı veya şifre yanlış')
            return redirect('loginUser')
            
    return render (request, 'user/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect ('index')


    

def registerUser(request):
    context={'title': 'Kayıt Ol'}
    if request.method == 'POST':
        name = request.POST['name']
        surname = request.POST['surname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if not User.objects.filter(username=username).exists():
                if not User.objects.filter(email=email).exists():
                    user = User.objects.create_user(first_name=name,last_name=surname,username=username,email=email,password=password1)
                    user.save()
                    userinfo =UserInfo(email=email,password=password1)
                    userinfo.save()
                    messages.success(request,'Kayıt Başarılı!!!')
                    return redirect('loginUser')
                else:
                    messages.warning(request,'Bu E-mail daha önceden kullanılmıştır.!')
                    return redirect('registerUser')
            else:
                messages.warning(request,'Bu kullanıcı Adı daha önceden kullanılmıştır.!')
                return redirect('registerUser')
        else:
            messages.warning(request,'Şifreler uyumsuz.!')
            return redirect('registerUser')
    return render (request,'user/register.html',context)

@login_required(login_url='/') #giriş yapmadan izin vermez
def browse(request):
    context={'title':'Profiller'}
    profils = Profil.objects.filter(user=request.user)
    if request.method == 'POST':
        if request.POST.get('button')=='buttonProfil':
            profilid = request.POST.get('profilid')
            profil = profils.get(id=profilid) #profili getir
            name = request.POST.get('name')
            image = request.FILES.get('image')
            if image is None:
                image = profil.image
            profil.name=name
            profil.image=image
            profil.save()
            return redirect('browse')
             
    if len(profils)<4:
        if request.method == 'POST':
            if request.POST.get('button')=='makeProfil':
                name= request.POST.get('name')
                image = request.FILES.get('image')
                if image is None:
                    image='profil/1.png'
                profil = Profil(name=name,image=image,user=request.user)
                profil.save()
        
                return redirect('browse')
    context.update({'profils':profils})
    return render (request,'user/browse.html',context)


def browseDel(request,pid):
    profil = Profil.objects.get(id=pid)
    profil.delete()
    return redirect('browse')
    

def hesap(request,hid):
    context={'title':'Hesap Ayarları'}
    profils = Profil.objects.filter(user = request.user)
    profil =Profil.objects.get(id=hid)
    userinfo = UserInfo.objects.get(user=request.user)
    user = User.objects.get(username=request.user)
    
    # hesap ayarları
    
    if request.method == 'POST':
        if request.POST.get('button') == 'emailChange':
            email = request.POST.get('email')
            user.email = email
            user.save()
            return redirect('/Hesap/'+hid+'/')
        
        elif request.POST.get('button') == 'passwordChange':
            password = request.POST.get('password')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            if password1 == password2:
                if user.check_password(password):
                    userinfo.password=password1
                    userinfo.save
                    
                    user.set_password(password1)
                    user.save()
                    
            return redirect ('loginUser')
        
        if request.POST.get('button') == 'telChange':
            tel =PhoneField.request.POST.get('tel')
            user.tel = tel
            user.save()
            return redirect('/Hesap/'+hid+'/')
       
    
    
    context.update({
        'profils':profils,
        'profil':profil,
        'userinfo':userinfo,
          
    })
    
    return render(request,'user/hesap.html',context)
    
def index2(request,categoryId):
    categorys = Category.objects.all()
    blog = Blog.objects.filter(category=categoryId)
    baslik = Category.objects.get(id=categoryId)
    context={
        "title":"Netflix",
        "blog":blog,
        "categorys":categorys,
        "baslik":baslik,    
    }
    return render(request, 'browse-index.html',context)
