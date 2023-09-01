from django.shortcuts import render

from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.request import Request
from .models import University,  StudyProgram
from .serializers import UniversitySerializer, StudyProgramSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class UniversityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows multiple members to be created.
    """
    queryset = University.objects.none()
    serializer_class = UniversitySerializer

    def get_queryset(self):
         queryset = University.objects.all()
         return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        results = University.objects.all()
        output_serializer = UniversitySerializer(results, many=True)
        data = output_serializer.data[:]
        return Response(data)
        

class StudyProgramViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows multiple members to be created.
    """
    queryset = StudyProgram.objects.none()
    serializer_class = StudyProgramSerializer

    def get_queryset(self):
         queryset = StudyProgram.objects.all()
         return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        results = StudyProgram.objects.all()
        output_serializer = StudyProgramSerializer(results, many=True)
        data = output_serializer.data[:]
        return Response(data)
        