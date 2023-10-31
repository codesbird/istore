from django.shortcuts import render,redirect
from file.models import Uploadfile,filesize
from django.contrib.auth.decorators import login_required
from django import forms
from file.forms import CustomAuthenticationForm
from django.contrib.auth import login, logout
from django.conf import settings
import os


@login_required
def index(request):
    
    if request.method =="POST":
        title = request.POST.get('title')
        Files = request.FILES['upload']
        
        datasize = filesize(Files)
        print("The File Size is : ",filesize)
        file   = Uploadfile.objects.create(title=title,file=Files,size = datasize)
        file.save()
        
    return render(request,'index.html')

    
    
@login_required
def Download(request):
    allfiles = Uploadfile.objects.all()
    print(open(allfiles[0].file.path.replace('\\\\','/'),'r'))
    
    return render(request,"download.html",{'files':allfiles})

    
def Login(request):
    return render(request,"login.html")


def Login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        print(form.errors)
            # return redirect('file_list')  # Redirect to your desired page after successful login
    else:
        form = CustomAuthenticationForm()
    
    # form.fields['username'] = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # form.fields['password'] = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
        
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the