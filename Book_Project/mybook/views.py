from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from mybook.models import BookModel
from .serializers import BookSerializers
from rest_framework import status
# Create your views here.


class BookCreate_API(APIView):
    def post(self, request):
        serializer = BookSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#READ(ALL BOOKS)
class BookRead_API(APIView):
    def get(self, request):
        books = BookModel.objects.all()
        serializer = BookSerializers(books, many=True)
        return Response(serializer.data)
    
    
    
#READ(SINGLE BOOKS)
class SingleBookRead_API(APIView):
    def get(self, request, id):
        try:
            single_book = BookModel.objects.get(id=id)
        except BookModel.DoesNotExist:
            raise Http404("Book not found...")
        serializer = BookSerializers(single_book)
        return Response(serializer.data)
    
    
    
    
    
#UPDATE 
class BookUpdate_API(APIView):
    def put(self, request, id):
        try:
            single_book = BookModel.objects.get(id=id)
        except BookModel.DoesNotExist:
            raise Http404("BOOK NOT FOUND....")
        serializer = BookSerializers(single_book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
#DELETE....
class BookDelete_API(APIView):
    def delete(self, request, id):
        try:
            single_book = BookModel.objects.get(id=id)
        except BookModel.DoesNotExist:
            raise Http404("BOOK NOT FOUND....")
        single_book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)