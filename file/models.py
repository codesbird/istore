from django.db import models
import os
from django.dispatch import receiver

class  Uploadfile(models.Model):
    title  = models.CharField(max_length=100,default="New Document")
    file  = models.FileField(upload_to='files')
    # thumb  = models.ImageField(upload_to='tumb')
    size = models.CharField(max_length=10,default='',blank=True)
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


# These two auto-delete files from filesystem when they are unneeded:

@receiver(models.signals.post_save, sender=Uploadfile)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.file:
        if os.path.isfile(instance.file.path):
            size = filesize(instance.file)
            instance.size = size
            

    

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
    
   