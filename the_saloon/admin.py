from django.contrib import admin
from django.contrib.auth.models import Group, User

# Unregister groups
admin.site.unregister(Group)



# Extend user model
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]

# Unregister initial user
admin.site.unregister(User)
# Reregister user
admin.site.register(User, UserAdmin)