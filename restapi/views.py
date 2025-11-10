from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from .models import Student
from .serializars import StudentSerializar
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
from .paginations import StudentPagination


@api_view(["GET"])
def get_data(request):
   
   student = Student.objects.all()
   pagenations = StudentPagination()
   data = pagenations.paginate_queryset(student, request)
   serializer = StudentSerializar(data, many=True)
   return Response(serializer.data, status=status.HTTP_200_OK)
   
   
class StudentList(APIView):
   """
   List all snippets, or create a new snippet.
   """

   def get(self, request, format=None):
        snippets = Student.objects.all()
        pagenations = StudentPagination()
        data = pagenations.paginate_queryset(snippets, request)
        serializer = StudentSerializar(data, many=True)
        return Response(serializer.data)

   def post(self, request, format=None):
        print("data", request.data)
        serializer = StudentSerializar(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
     
   def put(self, request,pk, format=None):
        print("data", request.data)
        serializer = StudentSerializar(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentListGenric(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializar
    pagination_class  = StudentPagination
    
class StudetRetUpDesGenric(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializar
    
class studentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = StudentSerializar
    queryset = Student.objects.all()
    pagination_class  = StudentPagination
    
    
# from rest_framework.pagination import PageNumberPagination

# class MyPagination(PageNumberPagination):
#     page_size = 5
#     page_query_param = 'page'
#     page_size_query_param = 'page_size'
#     max_page_size = 10  

# @api_view(['GET'])
# def student_list(request):
#     students = Student.objects.all().order_by('id')
#     paginator = StudentPagination()
#     paginated_students = paginator.paginate_queryset(students, request)
#     serializer = StudentSerializer(paginated_students, many=True)
#     return paginator.get_paginated_response(serializer.data)