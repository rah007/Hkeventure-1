from django.contrib import admin

# Register your models here.

from .models import Trek, Details

admin.site.register(Trek)
admin.site.register(Details)
