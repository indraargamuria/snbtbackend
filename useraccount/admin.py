from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
# Register your models here.
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(models.UserProfile)
class UserProfileAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('user','university1','studyprogram1','university2','studyprogram2')
