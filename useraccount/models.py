from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from ref import models as ref_models
# Create your models here.

class UserAccountManager(BaseUserManager):
    def create_superuser(self, email, fullname, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        return self.create_user(email, fullname, password, **other_fields)
    
    def create_user(self, email, fullname, password, **other_fields):

        email = self.normalize_email(email)
        user = self.model(email=email, fullname=fullname, **other_fields)
        user.set_password(password)
        user.save()
        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'),  unique=True)
    fullname = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname']

    def __str__(self) -> str:
        return self.fullname

class UserProfile(models.Model):

    genderoptions = (
        (1, 'Laki-Laki'),
        (2, 'Perempuan'),
    )
    schoolgradeoptions = (
        (1, '1 SMA'),
        (2, '2 SMA'),
        (3, '3 SMA'),
        (4, 'Alumni'),
    )
    schoolprogramoptions = (
        (1, 'Ilmu Pengetahuan Alam'),
        (2, 'Ilmu Pengetahuan Sosial'),
        (3, 'Bahasa'),
        (4, 'Agama'),
        (5, 'Teknik'),
        (6, 'Non Teknik'),
    )


    user = models.OneToOneField(
        UserAccount,
        on_delete=models.PROTECT,
        primary_key=True,
    )
    nickname = models.CharField(max_length=200)
    birthdate = models.DateField()
    gender = models.IntegerField(choices=genderoptions)
    phonenumber = models.CharField(max_length=100)
    instagramaccount = models.CharField(max_length=100)
    instagramfollower = models.IntegerField()
    schoolname = models.CharField(max_length=200)
    schoolgrade = models.IntegerField(choices=schoolgradeoptions)
    schoolprogram = models.IntegerField(choices=schoolprogramoptions)
    schoolfinishyear = models.CharField(max_length=10)
    university1 = models.ForeignKey(ref_models.University, on_delete=models.PROTECT, related_name="university1_related")
    studyprogram1 = models.ForeignKey(ref_models.StudyProgram, on_delete=models.PROTECT, related_name="studyprogram1_related")
    university2 = models.ForeignKey(ref_models.University, on_delete=models.PROTECT, related_name="university2_related")
    studyprogram2 = models.ForeignKey(ref_models.StudyProgram, on_delete=models.PROTECT, related_name="studyprogram2_related")
    studentnumber = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return str(self.user)

