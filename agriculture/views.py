from django.shortcuts import render,redirect
from .models import register,adminpanel,adminfruits,adminveg,admintubers,admingreens,soil,Red,Black,Alluvial,Sandy,Clay
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/login")
def nav(request,id):
    output = register.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        register.objects.filter(id=id).update(name=name,email=email,phone=phone)
        User.objects.filter(id=id).update(username=name,email=email)
        return redirect('home')
        # return render(request,'update.html',{'output': output})
    return render(request,'update.html',{'output':output})
 

@login_required(login_url="/login")
def profile(request):
    return render(request,'profile.html')

@login_required(login_url="/login")
def home(request):
    return render(request,'home.html')

@login_required(login_url="/login")
def dashboard(request):
    contents = adminpanel.objects.all()
    return render(request,'dashboard.html',{'contents':contents})

@login_required(login_url="/login")
def fruits(request):
    contents = adminfruits.objects.all()
    return render(request,'fruits.html',{'contents':contents})

@login_required(login_url="/login")
def vegs(request):
    contents = adminveg.objects.all()
    return render(request,'vegs.html',{'contents':contents})

@login_required(login_url="/login")
def tubers(request):
    contents = admintubers.objects.all()
    return render(request,'tubers.html',{'contents':contents})

@login_required(login_url="/login")
def greens(request):
    contents = admingreens.objects.all()
    return render(request,'greens.html',{'contents':contents})

def logininfo(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        #if name and password:
        user = auth.authenticate(username = name , password = password)
        if user is not None:
            auth.login(request,user)

            return redirect("/")
        else:
            messages.info(request,"Invalid Data")
            return redirect('login')
    else:
        return render(request,'login.html')

def registeration(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        conpassword = request.POST['conpassword']
        if User.objects.filter(email=email).exists():
            messages.info(request,'Email exists')
            return redirect('register')
        elif User.objects.filter(username=name).exists():
            messages.info(request,'Name exists')
            return redirect('register')
        elif (password != conpassword):
            messages.info(request,'Password Mismatch')
            return redirect('register')
        else:
            data = register(name=name,phone=phone,email=email,password=password)
            data.save()
            user = User.objects.create_user(username=name,password=password,email=email)
            user.save()
            return redirect('/login')
    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url="/login")
def viewdetail(request,name):
    if(name == 'CROP Cultivation' or name == 'Paddy'):
        return render(request,'crop.html')
    elif(name == 'FRUITS Cultivation'):
        return redirect('fruits')
    elif(name == 'TUBER Cultivation'):
        return redirect('tubers')
    elif(name == 'VEGETABLE Cultivation'):
        return redirect('vegs')
    elif(name == 'GREENS Cultivation'):
        return redirect('greens')

@login_required(login_url="/login")
def viewfruits(request,name):
    if(name == 'MANGO Cultivation' or name == 'Mango'):
        return render(request,'mango2.html')
    elif(name == 'GUAVA Cultivation' or name == 'Guava'):
        return render(request,'guva.html')
    else:
        return render(request,'pome.html')

@login_required(login_url="/login")
def viewtubers(request, name):
    if(name == 'BEETROOT Cultivation' or name == 'Beetroot'):
        return render(request,'betroot.html')
    elif(name == 'POTATO Cultivation' or name == 'Potato'):
        return render(request,'potato.html')
    else:
        return render(request,'carroot.html')

@login_required(login_url="/login")
def viewvegs(request,name):
    if(name == 'TOMATO Cultivation' or name == 'Tomato'):
        return render(request,'tomato.html')
    elif(name == 'CABBAGE Cultivation' or name == 'Cabbage'):
        return render(request,'cabbage.html')
    elif(name == 'CUCUMBER Cultivation' or name == 'Cucumber'):
        return render(request,'cucumber.html')

@login_required(login_url="/login")
def viewgreens(request,name):
    if(name == 'CURRY Cultivation' or name == 'Curry'):
        return render(request,'curry.html')
    elif(name == 'CORIANDER Cultivation' or name == 'Coriander'):
        return render(request,'coriander.html')
    elif(name == 'LETTUCE Cultivation' or name == 'Lettuce'):
        return render(request,'lettuce.html')

@login_required(login_url="/login")
def profile(request,id):
    output = register.objects.all()
    return render(request,'')

@login_required(login_url="/login")
def soilview(request):
    return render(request,'soil.html')


@login_required(login_url="/login")
def soiltypes(request):
    return (request,'')

@login_required(login_url="/login")
def Soiltypes(request):
    name = request.POST['soil']
    print(name)
       #print(contents.name)
        #return render(request,'soil1.html')
    #return render(request,'soil1.html')
    if(name == 'Red Soil'):
        contents = Red.objects.all()
        return render(request,'redsoil.html',{'contents':contents})
    if(name == 'Black Soil'):
        contents = Black.objects.all()
        return render(request,'redsoil.html',{'contents':contents})
    elif(name == 'Clay Soil'):
        contents = Clay.objects.all()
        return render(request,'redsoil.html',{'contents':contents})
    elif(name == 'Alluvial Soil'):
        contents = Alluvial.objects.all()
        return render(request,'redsoil.html',{'contents':contents})
    elif(name == 'Sandy Soil'):
        contents = Sandy.objects.all()
        return render(request,'redsoil.html',{'contents':contents})


