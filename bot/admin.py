from django.contrib import admin
from .models import BotUsers, BotAdmin
# Register your models here.
class CustomBotAdmin(admin.ModelAdmin):
    def user_list(self, obj):
        return ", ".join([str(user) for user in obj.user.all()])
    user_list.short_description = 'Users'

    list_display = ('id', 'user_list')
    
admin.site.register(BotUsers)
admin.site.register(BotAdmin, CustomBotAdmin)