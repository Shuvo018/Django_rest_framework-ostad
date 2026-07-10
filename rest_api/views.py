from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_api.models import Book
from rest_api.serializers import BookSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class BookView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        params = self.request.query_params
        title = params.get('title')
        price = params.get('price')
        if title:
            books = Book.objects.filter(title=title)
        elif price:
            books = Book.objects.filter(price=price)
        else:
            books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BookDetailView(APIView):
    def get(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(book, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(book, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(book, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)