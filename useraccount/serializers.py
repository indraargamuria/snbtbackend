from rest_framework import serializers
from .models import UserAccount

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
    

class MasterUserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount 
        fields = '__all__' 