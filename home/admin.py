from django.contrib import admin

# Register your models here.
from .models import JobListing,Category
class CatAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {'slug': ('title',)} 
class JobAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {'slug': ('title',)}     


admin.site.register(Category,CatAdmin)
admin.site.register(JobListing,JobAdmin)