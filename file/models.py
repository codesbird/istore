from django.db import models
from datetime import datetime

class  Uploadfile(models.Model):
    title  = models.CharField(max_length=100,default="New Document")
    file  = models.FileField(upload_to='files')
    thumb  = models.ImageField(upload_to='tumb')
    size = models.CharField(max_length=10,default='')
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


def filesize(file):
    x = file.size
    y = 512000
    if x < y:
        value = round(x/1000, 2)
        ext = ' kb'
    elif x < y*1000:
        value = round(x/1000000, 2)
        ext = ' Mb'
    else:
        value = round(x/1000000000, 2)
        ext = ' Gb'
    return str(value)+ext