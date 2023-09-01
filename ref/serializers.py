from rest_framework import serializers
from .models import University, StudyProgram



class StudyProgramSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = StudyProgram
        fields = '__all__' 
        


class UniversitySerializer(serializers.ModelSerializer):
    studyprogram_related = StudyProgramSerializer(many=True, read_only=True)
    class Meta:
        model = University
        fields = '__all__' 
        