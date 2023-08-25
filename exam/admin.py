from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from . import models
# Register your models here.
@admin.register(models.MasterPackage)
class MasterPackageAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','user','name','timeline','status')

admin.site.register(models.MasterTimeline)
@admin.register(models.MasterYear)
class MasterYearAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','year')

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

@admin.register(models.TransactUserPackage)
class TransactUserPackageAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','user','package','status','sectiondone')


@admin.register(models.TransactUserAnswer)
class TransactUserAnswerAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','user','userpackage','package','section','subtest','question','answer')