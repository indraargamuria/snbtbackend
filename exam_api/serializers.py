from rest_framework import serializers
from rest_framework.fields import empty
from rest_framework.permissions import AllowAny
from exam.models import TransactUserAnswer, MasterAnswer, MasterQuestion, MasterSubTest, MasterSection, TransactUserPackage, MasterPackage, MasterTimeline, MasterYear




class MasterAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterAnswer
        fields = '__all__' 
        

class MasterQuestionSerializer(serializers.ModelSerializer):
    answer_related = MasterAnswerSerializer(many=True, read_only=True)
    class Meta:
        model = MasterQuestion
        fields = '__all__' 
        

class MasterSubTestSerializer(serializers.ModelSerializer):
    question_related = MasterQuestionSerializer(many=True, read_only=True)
    class Meta:
        model = MasterSubTest
        fields = '__all__' 
        
class MasterSectionSerializer(serializers.ModelSerializer):
    subtest_related = MasterSubTestSerializer(many=True, read_only=True)
    class Meta:
        model = MasterSection
        fields = '__all__' 

class MasterPackageSerializer(serializers.ModelSerializer):
    section_related = MasterSectionSerializer(many=True, read_only=True)
    class Meta:
        model = MasterPackage
        fields = '__all__' 

class MasterTimelineSerializer(serializers.ModelSerializer):
    permission_classes = [AllowAny]
    package_related = MasterPackageSerializer(many=True, read_only=True)
    class Meta: 
        model = MasterTimeline
        # fields = ('id', 'name', 'year', 'month')  
        fields = '__all__' 

class TransactUserPackageSerializer(serializers.ModelSerializer):
    # package_related = MasterPackageSerializer(many=True, read_only=True)
    class Meta:
        model = TransactUserPackage 
        fields = '__all__' 


class TransactUserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactUserAnswer 
        fields = '__all__' 



class MasterYearSerializer(serializers.ModelSerializer):
    # timeline_related = MasterTimelineSerializer(many=True, read_only=True)
    # def __init__(self, *args, **kwargs):
    #     many = kwargs.pop('many',True)
    #     super(MasterYearSerializer,self).__init__(many=many, *args, **kwargs)
    
    class Meta:
        model = MasterYear
        fields = ('id', 'year')   
