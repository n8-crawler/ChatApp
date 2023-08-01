from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Room,Topic,Messages
from .forms import Roomform,Userform
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def loginform(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,'==>',password)
        try:
            User.objects.get(username=username)
            print('USER EXIST')
            return redirect(home)
        except:
            return HttpResponse('<h1>HI U ARE NOT A REGISTERED USER</h1>')

    return render(request,'loginform.html',{'page':page})

def logoutuser(request):
    logout(request)
    return redirect(home)   

def registeruser(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
    return render(request,'loginform.html',{'form':form})

def userprofile(request,pk):
    user = User.objects.get(id=pk) # user registered
    rooms = user.room_set.all() # rooms created by same user so user.room
    user_messages = user.messages_set.all()
    return render(request,'profile.html',{'user':user,'rooms':rooms,'user_messages':user_messages})

def updateuser(request,pk):
    profile = User.objects.get(id=pk)
    form = Userform()
    if request.method =='POST':
        form = Userform(request.POST,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request,'updateprofile.html',{'form':form})


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) | 
        Q(description__icontains=q)
        )
    topics = Topic.objects.all()

    return render(request,'home.html',{'rooms':rooms,'topics':topics})

def room(request,pk):
    rom = Room.objects.get(id=pk)
    #message is child of room since we have used its foreign key and we can get all messages classes created for the room
    #by using Room.messages_set.all() here Message class is in lowercase and set is a ORM mapper
    messages = rom.messages_set.all()
    participants = rom.participants.all()
    print(len(participants))
    #comments
    if request.method == 'POST':
        #create a comment/message
        Messages.objects.create(
            user = request.user,
            room = rom,
            body = request.POST.get('body')

        )
        rom.participants.add(request.user) 
        return redirect(room,pk=rom.id)

    return render(request,'room.html',{'rooms':rom,'messages':messages,'participants':participants})


@login_required(login_url='/login')
def create_room(request):
    form  = Roomform()
    if request.method == 'POST':
        form  = Roomform(request.POST)
        if form.is_valid():
            form.save()
        return redirect(home)

    return render(request,'createroom.html',context = {'form':form})

@csrf_exempt
@login_required(login_url='/login')
def update_room(request,pk):
    form  = Roomform()

    room  = Room.objects.get(id = pk)
    if room:
        form  = Roomform(instance=room)

        if request.method == 'POST':
            form = Roomform(request.POST,instance=room)
            if form.is_valid():
                form.save()
            return redirect(home)
    return render(request,'createroom.html',context = {'form':form})

@login_required(login_url='/login')
def delete_room(request,pk):

    room  = Room.objects.get(id = pk)
    if room:
        # form  = Roomform(instance=room)
        if request.method == 'POST':
            room.delete()
            return redirect(home)
    return render(request,'delete.html')

