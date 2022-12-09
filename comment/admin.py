from django.contrib import admin

# Register your models here.
# 导入Comment
from .models import Comment

admin.site.register(Comment)
