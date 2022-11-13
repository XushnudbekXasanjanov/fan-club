from django.shortcuts import render,redirect
from .models import *
def Index(request):
    return render(request,'index.html')

def Blogs(request):
    return render(request,'blog.html')

def Contact(request):
    return render(request,'contact.html')

def Matches(request):
    context = {
        'game':Match.objects.last(),
        'next':NextMatch.objects.last(),
        'all':AllMatchs.objects.all().order_by('-date')
    }
    return render(request,'matches.html',context)

def AllPlayers(request):
    context = {
        'player':Players.objects.all(),

    }
    return render(request,'players.html',context)

def BlogSingle(request):
    return render(request,'single.html')


