from django.contrib import admin
from .models import BlogCustomUser
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .forms import RegisterUserForm

class BlogCustomUserAdmin(UserAdmin):
	add_form = RegisterUserForm

	list_display = ('username', 'email' ,'bio','is_admin','date_joined')
	list_filter = ('is_admin','date_joined')

	fieldsets = (
		('User Info',{'fields':('username','email','bio','password','display_picture')}),
		('Permissions',{'fields':('is_admin',)})
		)
	search_fields = ('username','email')
	ordering = ('username','email')

	filter_horizontal = ()

	add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email','password1', 'password2','display_picture'),
        }),
    )



admin.site.register(BlogCustomUser,BlogCustomUserAdmin)
admin.site.unregister(Group)
