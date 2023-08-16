from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from . import models
# Register your models here.
@admin.register(models.MasterPackage)
class MasterPackageAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','user','name','timeline','status')

admin.site.register(models.MasterTimeline)
admin.site.register(models.MasterYear)

@admin.register(models.MasterSection)
class MasterSectionAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','name','package')

@admin.register(models.MasterSubTest)
class MasterSubTestAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','name','duration','section')

@admin.register(models.MasterQuestion)
class MasterQuestionAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','name','number','subtest')

@admin.register(models.MasterAnswer)
class MasterAnswerAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','name','order','isright','question')

admin.site.register(models.TransactUserPackage)