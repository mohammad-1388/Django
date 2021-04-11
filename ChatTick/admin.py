from django.contrib import admin

from ChatTick.models import Message, Group, MessageGroup


class AdminMessage(admin.ModelAdmin):
    search_fields = ["writer", "to_user"]
    list_display = ["writer", "to_user", "id"]


class AdminGroup(admin.ModelAdmin):
    search_fields = ["name", "admin_users", "users", "link"]
    list_display = ["name", "admin_users", "link", "id"]


class AdminMessageGroup(admin.ModelAdmin):
    search_fields = ["text"]
    list_display = ["writer", "id"]


admin.site.register(Message, AdminMessage)
admin.site.register(Group, AdminGroup)
admin.site.register(MessageGroup, AdminMessageGroup)
