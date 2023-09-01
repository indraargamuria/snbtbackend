from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from . import models

@admin.register(models.University)
class UniversityAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','name')

    
@admin.register(models.StudyProgram)
class StudyProgramAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','name','university')

