# from rest_framework import viewsets, generics
# from .models import Student
# from .serializer import StudentSerializer

# class StudentViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def perform_create(self, serializer):
#         serializer.save(created_by=self.request.user)

#     def perform_update(self, serializer):
#         serializer.save(modified_by=self.request.user)

# class StudentListCreateView(generics.ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer



from django.urls import path, include
from . import views

urlpatterns = [

    path("" , views.BlogPostListCreate.as_view(), name='blog_list_create'),
    path("blogposts/<int:pk>/",views.BlogPostRetrieveUpdateDestroy.as_view() , name="update" )

]
# from hello.views import StudentViewSet, StudentListCreateView
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'students', StudentViewSet)
    # path('', include(router.urls)),
    # path('students/', StudentListCreateView.as_view(), name='student_list_create'),