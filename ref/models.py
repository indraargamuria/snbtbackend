from django.db import models

# Create your models here.

class University(models.Model):

    name = models.CharField(max_length=300)
    
    def __str__(self) -> str:
        return str(self.name)


class StudyProgram(models.Model):

    name = models.CharField(max_length=300)
    university = models.ForeignKey(University, on_delete=models.PROTECT, related_name="studyprogram_related")
    
    def __str__(self) -> str:
        return str(self.name)
