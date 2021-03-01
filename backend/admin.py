from django.contrib import admin

from backend.models import *


class UserAdmin(admin.ModelAdmin):
    list_filter = ("teacher_request", )


admin.site.register(User, UserAdmin)
admin.site.register(Community)
admin.site.register(Post)
admin.site.register(PostComment)
admin.site.register(PostLike)
admin.site.register(PostCommentLike)
admin.site.register(CommunityMember)
