from django.contrib import admin
from .models import Profile, Record

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    def user_username(self, obj):
        return obj.user.username

class RecordAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Record, RecordAdmin)