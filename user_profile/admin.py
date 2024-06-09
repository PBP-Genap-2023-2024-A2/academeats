from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import UserProfile


class UserProfileAdmin(BaseUserAdmin):
    list_display = ('email', 'nomor_hp', 'username', 'nama_lengkap', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'nomor_hp', 'username', 'password')}),
        ('Personal info', {'fields': ('nama_lengkap', 'nama_panggilan', 'bio', 'saldo', 'pfp_url')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nomor_hp', 'username', 'password1', 'password2', 'role'),
        }),
    )
    search_fields = ('email', 'nomor_hp', 'username', 'nama_lengkap', 'nama_panggilan')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(UserProfile, UserProfileAdmin)
