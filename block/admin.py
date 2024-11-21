from django.contrib import admin

from .models import Post, Category, Comment

class CommentItemInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ('post',)
    


class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content'] 
    list_display = ('title', 'slug','category', 'created_on', 'status')
    list_filter = ('category', 'created_on', 'status')
    inlines = [CommentItemInline]
    prepopulated_fields = {'slug': ('title',)}
    
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title'] 
    list_filter = ('title','slug')
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    
    
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created_on')     
        
        

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
