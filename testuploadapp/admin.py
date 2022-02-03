from django.contrib import admin
from .models import person

# Register your models here.
class MobileAdmin(admin.ModelAdmin):
    list_display = ("firstname","lastname",)

admin.site.register(person,MobileAdmin)