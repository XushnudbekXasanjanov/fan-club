from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _

@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ['id','username', 'first_name','last_name', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Extra'), {'fields': ('types',)}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
admin.site.register(Team)
admin.site.register(Turnir)
admin.site.register(Match)
admin.site.register(NextMatch)
admin.site.register(AllMatchs)
admin.site.register(Players)
admin.site.register(Blogs)
admin.site.register(CategoryBlogs)
admin.site.register(Contact)
admin.site.register(Table)
