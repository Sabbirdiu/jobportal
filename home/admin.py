from django.contrib import admin

# Register your models here.
from .models import JobListing,Category,ApplyJob,Favorite
class CatAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {'slug': ('title',)} 
class JobAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {'slug': ('title',)}     

class ApplyAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'email', 'file') 
    list_filter = ('name', 'email') 
    search_fields = ('name', 'email') 
admin.site.register(Category,CatAdmin)
admin.site.register(JobListing,JobAdmin)
admin.site.register(ApplyJob,ApplyAdmin)
admin.site.register(Favorite)