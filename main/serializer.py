from rest_framework import serializers
from.models import *



class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"



class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = "__all__"



class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = "__all__"


    
class FacultiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculties
        fields = "__all__"



class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = "__all__"



class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = "__all__"



class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = "__all__"


    

class P_UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = P_University
        fields = "__all__"



class SingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Single
        fields = "__all__"



class AssistentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistent
        fields = "__all__"



class U_CabinetSerializer(serializers.ModelSerializer):
    class Meta:
        model = U_Cabinet
        fields = "__all__"



class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search
        fields = "__all__"