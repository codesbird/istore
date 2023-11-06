from django.db import models
import os
from django.dispatch import receiver
from django.contrib.auth.models import User

class  Uploadfile(models.Model):
    title  = models.CharField(max_length=100,default="New Document")
    file  = models.FileField(upload_to='files')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='userprofile',blank=True,null=True)
    downloadid = models.FloatField(default=0.0)
    fileid = models.FloatField(default=0.0)
    size = models.CharField(max_length=10,default='',blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


def filesize(file):
    byte_value = file.size
    if byte_value!=0:
       
        if byte_value < 1024:
            value =byte_value 
            ext = "By"

        elif byte_value < 1024**2:
            value =byte_value / 1024
            ext = "KB"

        elif byte_value < 1024**3:
            value =byte_value / (1024**2)
            ext = "MB"

        elif byte_value < 1024**4:
            value =byte_value / (1024**3)
            ext = "GB"
        else:
            value =byte_value / (1024**4)
            ext = "TB"
            
        return [f"{value:.2f} {ext}",True]
    else:
        return ['',False]


# These two auto-delete files from filesystem when they are unneeded:
    

@receiver(models.signals.post_delete, sender=Uploadfile)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)

    
@receiver(models.signals.pre_save, sender=Uploadfile)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = Uploadfile.objects.get(pk=instance.pk).file
        
    except Uploadfile.DoesNotExist:
        return False

    new_file = instance.file
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
    
   