from fileupload.models import Picture
from django.contrib import admin

class PictureAdmin(admin.ModelAdmin):
    list_display = ('__unicode__',)

admin.site.register(Picture, PictureAdmin)
