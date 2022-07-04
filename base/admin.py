from django.contrib import admin
from .models import *
from embed_video.admin import AdminVideoMixin

class TutorialMediaAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(TutorialMedia, TutorialMediaAdmin)
admin.site.register(Tutorial)
admin.site.register(EnrolledTutorial)
