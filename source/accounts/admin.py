from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from accounts.models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    fields = ('birth_date', 'avatar')

class ProfileUserAdmin(UserAdmin):
    inlines = (ProfileInline,)


User = get_user_model()
admin.site.unregister(User)
admin.site.register(User, ProfileUserAdmin)
