from django.shortcuts import render

# Create your views here.
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterUserSerializer, MasterUserAccountSerializer
from .models import UserAccount
from rest_framework.permissions import AllowAny

class RegisterUserAccount(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        reg_serializer = RegisterUserSerializer(data=request.data)
        if reg_serializer.is_valid():
            newuser = reg_serializer.save()
            if newuser:
                return Response(status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class MasterUserAccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows multiple members to be created.
    """
    queryset = UserAccount.objects.none()
    serializer_class = MasterUserAccountSerializer

    def get_queryset(self):
         queryset = UserAccount.objects.all()
         return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        results = UserAccount.objects.all()
        output_serializer = MasterUserAccountSerializer(results, many=True)
        data = output_serializer.data[:]
        return Response(data)
        
    