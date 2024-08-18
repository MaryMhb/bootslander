from django.contrib import admin

# Register your models here.
from landing.models import User
class UserAdmin (admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('username' ,'email','created_date')
    list_filter = ('email',)
    search_fields = ['username',]
admin.site.register(User,UserAdmin)
