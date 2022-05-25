from django.contrib import admin

from theory.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display= ('title', 'status', 'datetime_modified')

admin.site.register(Post, PostAdmin)
