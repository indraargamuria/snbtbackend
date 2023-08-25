from django.db import models
# from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.conf import settings
from datetime import datetime
# Create your models here.

class MasterYear(models.Model):
    year = models.IntegerField()

    def __str__(self) -> str:
        return str(self.year)

class MasterTimeline(models.Model):
    statusoption = (
        (1, 'Activated'),
        (2, 'Deactivated'),
    )
    monthoption = (
        (1, 'January'),
        (2, 'February'),
        (3, 'March'),
        (4, 'April'),
        (5, 'May'),
        (6, 'June'),
        (7, 'July'),
        (8, 'August'),
        (9, 'September'),
        (10, 'October'),
        (11, 'November'),
        (12, 'December'),
    )

    name = models.CharField(max_length=100)
    year = models.ForeignKey(MasterYear, on_delete=models.PROTECT, related_name="timeline_related")
    month = models.IntegerField(choices=monthoption)
    status = models.IntegerField(choices=statusoption)
    registerdate = models.DateField(default=datetime.now)
    activitydate = models.DateField(default=datetime.now)
    announcementdate = models.DateField(default=datetime.now)
    liveclassdate = models.DateField(default=datetime.now)

    def __str__(self) -> str:
        return self.name

class MasterPackage(models.Model):

    class MasterPackageObject(models.Manager):
        def get_queryset(self) -> QuerySet:
            return super().get_queryset().filter(status=1)

    statusoption = (
        (1, 'Activated'),
        (2, 'Deactivated'),
    )

    timeline = models.ForeignKey(MasterTimeline, on_delete=models.PROTECT, related_name="package_related")
    name = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.IntegerField(choices=statusoption)
    objects = models.Manager() #Default Manager - Display All Data
    masterpackageobjects = MasterPackageObject() #Custom Manager - Display Filtered

    class Meta:
        ordering = ('-created',)

    def __str__(self) -> str:
        return self.name

class MasterSection(models.Model):

    package = models.ForeignKey(MasterPackage, on_delete=models.PROTECT, related_name="section_related")
    name = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name
    
class MasterSubTest(models.Model):

    section = models.ForeignKey(MasterSection, on_delete=models.PROTECT, related_name="subtest_related")
    name = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    duration = models.IntegerField()
    
    def __str__(self) -> str:
        return self.name
    
class MasterQuestion(models.Model):

    statusoption = (
        (1, 'Multiple Choice'),
        (2, 'True False'),
        (3, 'Multiple Check'),
    )

    subtest = models.ForeignKey(MasterSubTest, on_delete=models.PROTECT, related_name="question_related")
    name = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    type = models.IntegerField(choices=statusoption)
    number = models.IntegerField()
    
    def __str__(self) -> str:
        return self.name
    
class MasterAnswer(models.Model):

    question = models.ForeignKey(MasterQuestion, on_delete=models.PROTECT, related_name="answer_related")
    name = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    isright = models.IntegerField()
    order = models.IntegerField()
    
    def __str__(self) -> str:
        return self.name

class TransactUserPackage(models.Model):

    statusoption = (
        (1, 'Ready'),
        (2, 'Done'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_related")
    package = models.ForeignKey(MasterPackage, on_delete=models.PROTECT, related_name="package_related")
    status = models.IntegerField(choices=statusoption)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    sectiondone = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return str(self.package)

class TransactUserAnswer(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_transact_related")
    userpackage = models.ForeignKey(TransactUserPackage, on_delete=models.PROTECT, related_name="userpackage_related")
    package = models.ForeignKey(MasterPackage, on_delete=models.PROTECT, related_name="package_transact_related")
    section = models.ForeignKey(MasterSection, on_delete=models.PROTECT, related_name="section_transact_related")
    subtest = models.ForeignKey(MasterSubTest, on_delete=models.PROTECT, related_name="subtest_transact_related")
    question = models.ForeignKey(MasterQuestion, on_delete=models.PROTECT, related_name="question_transact_related")
    answer = models.ForeignKey(MasterAnswer, on_delete=models.PROTECT, related_name="answer_transact_related")

    
    def __str__(self) -> str:
        return str(self.userpackage)

