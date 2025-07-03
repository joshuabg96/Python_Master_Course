from django.contrib import admin
from .models import Post

# How we can modify the models by default, extended Post admin
class PostAdmin(admin.ModelAdmin):
    # Show at the moment of create a new entry
    readonly_fields = ('created','modified')
    #Show columns at the moment of we see all the entries
    list_display = ('title', 'created', 'modified')
    # Add date filter
    date_hierarchy = 'created'

# Register your models here.
admin.site.register(Post, PostAdmin)

