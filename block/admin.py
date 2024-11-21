from django.contrib import admin
from .models import Post,Category

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content'] 
    list_display = ('title', 'slug','category', 'created_on')
    list_filter = ('category', 'created_on')
        

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
