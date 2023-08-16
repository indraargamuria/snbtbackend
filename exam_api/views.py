# from django.shortcuts import render

# Create your views here.

from rest_framework import generics, viewsets
from rest_framework.response import Response
from exam.models import TransactUserPackage, MasterPackage, MasterTimeline, MasterYear
from .serializers import MultiPackageSerializer, TransactUserPackageSerializer, MasterPackageSerializer, MasterTimelineSerializer, MasterYearSerializer
from rest_framework.permissions import IsAuthenticated

class MasterYearList(generics.ListCreateAPIView):
    queryset = MasterYear.objects.all()
    serializer_class = MasterYearSerializer
    pass


# class MasterYearList(viewsets.ViewSet):
#     queryset = MasterYear.objects.all()
#     # serializer_class = MasterYearSerializer
#     def list(self,request):
#         serializer_class = MasterYearSerializer(self.queryset, many=True)
#         return Response(serializer_class.data)
    
    

class MasterTimelineList(generics.ListCreateAPIView):
    queryset = MasterTimeline.objects.all()
    serializer_class = MasterTimelineSerializer
    pass

class MasterPackageList(generics.ListCreateAPIView):
    # permission_classees = [IsAuthenticated]
    queryset = MasterPackage.masterpackageobjects.all()
    serializer_class = MasterPackageSerializer
    pass

class MasterPackageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MasterPackage.objects.all()
    serializer_class = MasterPackageSerializer
    pass


class TransactUserPackageList(generics.ListCreateAPIView):
    # permission_classees = [IsAuthenticated]
    queryset = TransactUserPackage.objects.all()
    serializer_class = TransactUserPackageSerializer
    pass

class MultiPackageViewSet(viewsets.ModelViewSet):
    """This view provides list, detail, create, retrieve, update
    and destroy actions for Things."""
    model = MasterPackage
    serializer_class = MultiPackageSerializer