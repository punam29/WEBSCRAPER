from django.contrib import admin
from app.models import Web


# Register your models here.
class WebAdmin(admin.ModelAdmin):
    list_display=['hrefvalue','linkname']



admin.site.register(Web,WebAdmin)