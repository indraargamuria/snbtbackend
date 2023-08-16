from django.urls import path
from .views import RegisterUserAccount  

app_name = 'useraccount'

urlpatterns = [
    path('register/', RegisterUserAccount.as_view(), name='createuser'),
]