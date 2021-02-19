from django.contrib import admin

from backend.models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Community)
admin.site.register(Post)
admin.site.register(PostComment)
admin.site.register(PostLike)
admin.site.register(PostCommentLike)
admin.site.register(CommunityMember)
