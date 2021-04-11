from django.contrib import admin

from accounts.models import Profile, GroupUsers, VisitsUsers, LikesUsers, AdminUsers, MuteUsers, CancelUsers, \
    BlockedUsers

admin.site.register(Profile)
admin.site.register(GroupUsers)
admin.site.register(VisitsUsers)
admin.site.register(LikesUsers)
admin.site.register(AdminUsers)
admin.site.register(MuteUsers)
admin.site.register(CancelUsers)
admin.site.register(BlockedUsers)
