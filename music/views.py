from django.shortcuts import render,redirect
from .models import Smusic,Like,Singers
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.db.models import Q,F
# Create your views here.
def mainlogin(request):
    if request.method=='GET':
        return render(request,'mainlogin.html')


def signup(request):
    if request.method=='GET':
        return render(request,'signup.html')
    if request.method=='POST':
        try:
            username=request.POST['username']
            email=request.POST['email']
            password=request.POST['password']
        except Exception:
            msg='enter detail correctly'
            return render(request,'signup.html',{'error':msg})
        

        if User.objects.filter(username=username).exists():
            msg='Username is already existed'
            return render(request,'signup.html',{'error':msg})
        if User.objects.filter(email=email).exists():
            msg='Mail is already Existed'
            return render(request,'signup.html',{'error':msg})
        user=User.objects.create_user(username=username,email=email,password=password)
        user.save()
        return redirect('userlogin')

def adminsignup(request):
    if request.method=='GET':
        return render(request,'adminsignup.html')
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(username=username).exists():
            msg='Username is already Exists'
            return render(request,'signup.html',{'error':msg})
        if User.objects.filter(email=email).exists():
            msg='Email already exists'
            return render(request,'signup.html',{'error':msg})
        superuser=User.objects.create_superuser(username=username,email=email,password=password)
        superuser.save()
        return redirect('adminlogin')
        
        

#User Login/Logout Logic
def userlogin(request):
    if request.method=='GET':
        return render(request,'userlogin.html')
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        valid_obj=authenticate(request,username=username,password=password)
        if valid_obj is None:
            msg='Password or User Name is Incorrect'
            return render(request,'userlogin.html',{'msg':msg})
        else:
            login(request,valid_obj)
            return redirect('select')
        
def userlogout(request):
    logout(request)
    return redirect('userlogin')




#Admin Login/Logout Logic
def adminlogin(request):
    if request.method=='GET':
        return render(request,'adminlogin.html')
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        valid_obj=authenticate(request,username=username,password=password)
        if valid_obj is None:
            msg='Password or User Name is Incorrect'
            return render(request,'userlogin.html',{'msg':msg})
        else:
            login(request,valid_obj)
            return redirect('insert')
def adminlogout(request):
    logout(request)
    return redirect('adminlogin')
        


#Only Admin Can Access This Page
#Inserting data to the database
@user_passes_test(lambda u: u.is_superuser)
def insert(request):
    if request.method=='GET':
        msg='you had no permission'
        return render(request,'insert.html',{'msg':msg})
    if request.method=='POST':
        try:
            sid=int(request.POST['songid'])
            sname=request.POST['songname']
            mname=request.POST['moviename']
            genre=request.POST['genre']
            siname=request.POST['singername']
            song=request.FILES['song']
            image=request.FILES['image']
            obj=Smusic.objects.create(songid=sid,songname=sname,moviename=mname,genre=genre,singername=siname,song=song,image=image)
            return render(request,'insert.html')
        
        except Exception:
            return render(request,'insert.html',{'error':'Enter Correct Details.Try Again'})


#Only Admin Can Access This Page
#Inserting data to the database
@user_passes_test(lambda u: u.is_superuser)
def insert2(request):
    if request.method=='GET':
        return render(request,'insert2.html')
    if request.method=='POST':
        singerid=int(request.POST['sid'])
        singername=request.POST['sname']
        image=request.FILES['simage']
        genre=request.POST['genre']
        Singers.objects.create(singerid=singerid,singername=singername,image=image,genre=genre)
        return render(request,'insert2.html',)




#Home Page Logic/Reading the Data From the DataBase
@login_required(login_url='userlogin')
def select(request):
    if request.method=='GET':
        sobj=Smusic.objects.filter(genre__icontains='devotional')
        pobj=Smusic.objects.filter(genre__icontains='phonk')
        fobj=Smusic.objects.filter(genre__icontains='telangana folk song')
        obj2=Like.objects.all()
        trending=Smusic.objects.order_by('-songid')[:23]
        singer=Singers.objects.all()
        return render(request,'select.html',{'sobj':sobj,'pobj':pobj,'fobj':fobj,'obj2':obj2,'trending':trending,'singer':singer})
    if request.method=='POST':
        search=request.POST['search']
        obj=Smusic.objects.filter(Q(genre__icontains=search) | Q(songname__icontains=search) | Q(singername__icontains=search) |Q(moviename__icontains=search))
        return render(request,'search.html',{'obj':obj})




#Filtering the data by searching
@login_required(login_url='userlogin')
def search(request):
    if request.method=='GET':
        return render(request,'search.html')
    if request.method=='POST':
        search=request.POST['search']
        obj=Smusic.objects.filter(Q(genre__icontains=search) | Q(songname__icontains=search) | Q(singername__icontains=search) |Q(moviename__icontains=search))
        return render(request,'search.html',{'obj':obj})





#Song Detail Page
@login_required(login_url='userlogin')
def detail(request,sid,sname):
    if request.method=='GET':
        obj=Smusic.objects.filter(songid=sid)
        obj1=Smusic.objects.filter(genre__icontains=sname)
        return render(request,'detail.html',{'obj':obj,'obj1':obj1})



#Singer details page
@login_required(login_url='userlogin')
def singerdetail(request,sid,sname):
    if request.method=='GET':
        obj=Singers.objects.filter(singerid=sid)
        obj1=Smusic.objects.filter(singername__icontains=sname)
        return render(request,'singerdetail.html',{'obj':obj,'obj1':obj1})



#Liking a Song Logic
@login_required(login_url='userlogin')
def like(request,sid):
    if request.method=='GET':
        obj=Smusic.objects.filter(songid=sid)
        return render(request,'like.html',{'obj':obj})
    if request.method=='POST':
        if Like.objects.filter(songid=sid).exists():
            msg='This Song already Exists'
            return render(request,'like.html',{'msg':msg})
        else:
            obj=Smusic.objects.filter(songid=sid)
            for i in obj:
                Like.objects.create(songid=i.songid,songname=i.songname,moviename=i.moviename,genre=i.genre,singername=i.singername,song=i.song,image=i.image)
        return redirect('select')



#Disliking the Song Logic
@login_required(login_url='userlogin')
def dislike(request,sid):
    if request.method=='GET':
        obj=Like.objects.filter(songid=sid)
        return render(request,'dislike.html',{'obj':obj})
    if request.method=='POST':
        if Like.objects.filter(songid=sid).exists():
            obj=Like.objects.filter(songid=sid)
            obj.delete()        
            return redirect('likepage')
            
        else:
            msg='No song To delete'
            return render(request,'dislike.html',{'msg':msg})      
        


#Likepage Logic  
@login_required(login_url='userlogin')
def likepage(request):
    if request.method=='GET':
        obj=Like.objects.all()
        return render(request,'likepage.html',{'obj':obj})


@login_required(login_url='userlogin')
def trending(request):
    if request.method=='GET':
        obj=Smusic.objects.order_by('-songid')[:25]
        return render(request,'trending.html',{'obj':obj}) 

@login_required(login_url='userlogin')
def phonk(request):
    if request.method=='GET':
        obj=Smusic.objects.filter(genre__icontains='phonk')
        return render(request,'phonk.html',{'obj':obj})

def add(request):
    pass
