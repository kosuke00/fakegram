from django.contrib import admin
# Register your models here.
from .models import *
from .forms import *

class ImageUploadAdmin(admin.ModelAdmin):
    form = ImageUpload
    model = Gram
    list_display = ["Photo"]
class CommentInline(admin.TabularInline):
    model = Reply
    extra = 0

class GramAdmin(admin.ModelAdmin):
    inlines = [
    CommentInline,
    ]

admin.site.register(Gram,ImageUploadAdmin)
admin.site.register(Reply)
