from django.contrib import admin
from core import models

# Register your models here.

admin.site.register(models.Category)
admin.site.register(models.Author)
admin.site.register(models.Comment)
admin.site.register(models.Blog)