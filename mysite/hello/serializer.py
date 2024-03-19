from rest_framework import serializers
from .models import blogpost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = blogpost # Specify the associated model
        fields = '__all__'

        
# from .models import Student

# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = '__all__'