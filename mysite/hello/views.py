from rest_framework import viewsets, generics
from .models import blogpost
from .serializer import BlogPostSerializer

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = blogpost.objects.all()
    serializer_class = BlogPostSerializer

class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = blogpost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "pk"


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