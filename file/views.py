from django.shortcuts import render,redirect,HttpResponse
from file.models import Uploadfile,filesize
from django.contrib.auth.decorators import login_required
from django import forms
from file.forms import CustomAuthenticationForm,UploadfilesForm
from django.contrib.auth import login, logout
from django.conf import settings
import time,io


@login_required
def index(request):
    
    if request.method =="POST":
        downloadid  = time.time()
        
        form = UploadfilesForm(request.POST,request.FILES)
        if form.is_valid():
            print("THis form is valid ")
            fields = form.fields

            instans  = form.save(commit=False)
            instans.downloadid = downloadid
            instans.size = filesize(request.FILES['file'])
            instans.save()
            
            instance = form.save(commit=False)
            # Set additional attributes before saving
            instance.size = filesize(instance.file)[0]  # Replace with your desired value
            instance.downloadid = downloadid # Replace with your desired value
            instance.fileid = time.time() # Replace with your desired value
            instance.user = request.user  # Assuming you are using Django's User model
            instance.save()
            
            print(instans)

        
    
    else:
        form = UploadfilesForm()
    

    return render(request,'index.html',{'form':form})

    
    
@login_required
def Download(request):
    allfiles = Uploadfile.objects.filter(user=request.user).values()
    filetypes = []
    
    for item in allfiles:
        item['type'] = item['file'].split('.')[-1].upper()
        filetypes.append(item['type'])
        
    return render(request,"download.html",{'files':allfiles,'filetypes':set(filetypes)})

    

def Login(request):
    if request.user.is_authenticated:
        return redirect('download')
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
  
        
    return render(request, 'login.html', {'form': form})

def DeleteItem(request,id):
    print("The item id is : ",id)
    if request.method=="POST":
        item  = Uploadfile.objects.filter(fileid=id).delete()
        print("The item is  : ",item)

    return redirect('download')

def DownloadItem(request,id):
    print("The item id is : ",id)
    
    if request.method=="POST":
        item  = Uploadfile.objects.filter(downloadid=id)

        response = HttpResponse(item[0].file.url, content_type='*/*')
        
        response['Content-Disposition'] = f'filename="QR-Code-getqrcode-view.png"'

        return redirect(f"/media/{item[0].file}")

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the

def ShareFile(request):
    
    return 