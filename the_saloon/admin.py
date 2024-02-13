from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, Shout
# Unregister groups
admin.site.unregister(Group)

# User and profile in same place
class ProfileInline(admin.StackedInline):
	    model = Profile

# Extend user model
class UserAdmin(admin.ModelAdmin):
        model = User
        # Just display username fields on admin page
        fields = ["username"]
        inlines = [ProfileInline]

# Unregister initial user
admin.site.unregister(User)
# Reregister user/profile
admin.site.register(User, UserAdmin)
admin.site.register(Profile)

# Register shouts
admin.site.register(Shout)