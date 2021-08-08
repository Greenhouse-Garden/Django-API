'''Users admin config site'''

#Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


#Models
from django.contrib.auth.models import User
from users.models import Profile


@admin.register(Profile)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'address', 'postalCode', 'city', 'country', 'phoneNumber', 'cc_number', 'cc_expiry', 'cc_code')
    list_display_links = ['id', 'user']
    list_editable = ['address', 'postalCode', 'country', 'city', 'phoneNumber', 'cc_number', 'cc_expiry', 'cc_code']
    search_fields = ['user__email', 'user__is_staff', 'created_at', 'modified_at']
    list_filter = ['user__is_active', 'user__is_staff', 'created_at', 'modified_at']


class ProfileInline(admin.StackedInline):
    
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'
    
class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff']
    list_editable = ['is_active', 'is_staff']
    
    
admin.site.unregister(User)
admin.site.register(User, UserAdmin)



