# from django.shortcuts import render

# Create your views here.

from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.request import Request
from exam.models import TransactUserAnswer, TransactUserPackage, MasterPackage, MasterTimeline, MasterYear
from .serializers import TransactUserAnswerSerializer, TransactUserPackageSerializer, MasterPackageSerializer, MasterTimelineSerializer, MasterYearSerializer
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


# class TransactUserPackageList(generics.ListCreateAPIView):
#     # permission_classees = [IsAuthenticated]
#     queryset = TransactUserPackage.objects.all()
#     serializer_class = TransactUserPackageSerializer
#     pass

# class MultiPackageViewSet(viewsets.ModelViewSet):
#     """This view provides list, detail, create, retrieve, update
#     and destroy actions for Things."""
#     model = MasterPackage
#     serializer_class = MultiPackageSerializer



class TransactUserPackageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows multiple members to be created.
    """
    queryset = TransactUserPackage.objects.none()
    serializer_class = TransactUserPackageSerializer

    def get_queryset(self):
         queryset = TransactUserPackage.objects.all()
         return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        results = TransactUserPackage.objects.all()
        output_serializer = TransactUserPackageSerializer(results, many=True)
        data = output_serializer.data[:]
        return Response(data)
    

class TransactUserAnswerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows multiple members to be created.
    """
    queryset = TransactUserAnswer.objects.none()
    serializer_class = TransactUserAnswerSerializer

    def get_queryset(self):
         queryset = TransactUserAnswer.objects.all()
         return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        results = TransactUserAnswer.objects.all()
        output_serializer = TransactUserAnswerSerializer(results, many=True)
        data = output_serializer.data[:]
        return Response(data)
        
    
# class YearViewSet(viewsets.ModelViewSet):
#     """This view provides list, detail, create, retrieve, update
#     and destroy actions for Things."""
#     queryset = MasterYear.objects.all()
#     serializer_class = TestYearSerializer

    
#     def get_serializer(self, *args, **kwargs):
#         if "data" in kwargs:
#             data = kwargs["data"]

#             # check if many is required
#             if isinstance(data, list):
#                 kwargs["many"] = True

#         return super(YearViewSet, self).get_serializer(*args, **kwargs)
