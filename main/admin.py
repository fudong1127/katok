from django.contrib import admin
import models
from django.conf import settings
from katok.main.models import Record

admin.site.register(Record)

class GalleryAdmin(admin.ModelAdmin):
    pass

class FotoAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Gallery, GalleryAdmin)
admin.site.register(models.Foto, FotoAdmin)