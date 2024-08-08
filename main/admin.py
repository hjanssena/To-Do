from django.contrib import admin
from .models import entry, tag

# Register your models here.
admin.site.register(entry)
admin.site.register(tag)