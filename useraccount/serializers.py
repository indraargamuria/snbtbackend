from rest_framework import serializers
from .models import UserAccount, UserProfile, MasterStudentNumber
from ref.models import University, StudyProgram

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('email','fullname','password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

 
class UniversitySerializer(serializers.ModelSerializer):

    
    class Meta:
        model = University 
        fields = '__all__' 


class StudyProgramSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = StudyProgram 
        fields = '__all__' 


class MasterUserProfileRawSerializer(serializers.ModelSerializer):
    
    # fullname = serializers.CharField(source='user.fullname')

    class Meta:
        model = UserProfile 
        fields = '__all__' 

class MasterUserProfileSerializer(serializers.ModelSerializer):
    
    university1_name = serializers.CharField(source='university1.name')
    studyprogram1_name = serializers.CharField(source='studyprogram1.name')
    university2_name = serializers.CharField(source='university2.name')
    studyprogram2_name = serializers.CharField(source='studyprogram2.name')


    class Meta:
        model = UserProfile 
        fields = '__all__' 

class MasterUserAccountSerializer(serializers.ModelSerializer):
    
    user_profile_related = MasterUserProfileSerializer(many=True, read_only=True)

    class Meta:
        model = UserAccount 
        fields = ('id','fullname','created','user_profile_related')


class MasterStudentNumberSerializer(serializers.ModelSerializer):
    


    class Meta:
        model = MasterStudentNumber 
        fields = '__all__' 
