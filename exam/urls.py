from django.urls import path
from django.views.generic import TemplateView

app_name = 'exam'

urlpatterns = [
    path('', TemplateView.as_view(template_name="exam/index.html")),
]