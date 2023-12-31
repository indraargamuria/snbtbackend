from django.urls import path
from .views import MasterTimelineList, MasterYearList, MasterPackageList, MasterPackageDetail

app_name = 'exam_api'

urlpatterns = [
    path('package/<int:pk>/', MasterPackageDetail.as_view(), name='detailcreate'),
    path('package/', MasterPackageList.as_view(), name='listcreate'),
    path('timeline/', MasterTimelineList.as_view(), name='listcreate'),
    path('year/', MasterYearList.as_view(), name='listcreate'),
    # path('multipackage/', MultiPackageViewSet.as_view({'post': 'create'}), name='listcreate'),
]