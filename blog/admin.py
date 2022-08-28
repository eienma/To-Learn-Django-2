from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author') #过滤
    search_fields = ('title', 'body') #搜索局域网
    prepopulated_fields = {'slug': ('title',)} #slug会自动填充
    raw_id_fields = ('author',) #搜索作者而非下拉菜单
    date_hierarchy = 'publish' #右边的日期层次结构
    ordering = ('status', 'publish') #默认排序

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')