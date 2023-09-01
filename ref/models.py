from django.db import models

# Create your models here.

class University(models.Model):

    name = models.CharField(max_length=300)
    province = models.CharField(max_length=300, null=True)
    
    def __str__(self) -> str:
        return str(self.name)


class StudyProgram(models.Model):

    name = models.CharField(max_length=300)
    university = models.ForeignKey(University, on_delete=models.PROTECT, related_name="studyprogram_related")
    code = models.CharField(max_length=300, null=True)
    minimumvalue = models.DecimalField(decimal_places=2, max_digits=18, default=0)
    
    def __str__(self) -> str:
        return str(self.name)
