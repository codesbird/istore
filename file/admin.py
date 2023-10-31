from django.contrib import admin
from file.models import Uploadfile
from django.contrib import admin


class AuthorAdmin(admin.ModelAdmin):
    model = Uploadfile
    list_display = ('title', 'file','size','date')
    
    search_fields = ['title']

admin.site.register(Uploadfile, AuthorAdmin)
