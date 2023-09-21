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


@admin.register(models.TemplateLoaderPackage)
class TemplateLoaderPackageAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','ipackage','isection','isubtest','iquestionnumber','iquestiontype','iquestiondescription'
                    ,'ianswer1','ianswer2','ianswer3','ianswer4','ianswer5'
                    ,'ianswer6','ianswer7','ianswer8','ianswer9','ianswer10')