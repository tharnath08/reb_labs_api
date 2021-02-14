from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Products
from .models import Categories
from .serializers import productSerializer, categorySerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class productlist(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        product = Products.objects.all()
        serializer = productSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        return Response({
                        "code":"authentication_error",
                        "message": "The API key provided does not have write permissions.",
                        "data":{"status": '401'}
                        }, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        return Response({
                        "code":"authentication_error",
                        "message": "The API key provided does not have write permissions.",
                        "data":{"status": '401'}
                        }, status=status.HTTP_400_BAD_REQUEST)


class categorylist(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        category = Categories.objects.all()
        serializer = categorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        return Response({
                        "code":"authentication_error",
                        "message": "The API key provided does not have write permissions.",
                        "data":{"status": '401'}
                        }, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        return Response({
                        "code":"authentication_error",
                        "message": "The API key provided does not have write permissions.",
                        "data":{"status": '401'}
                        }, status=status.HTTP_400_BAD_REQUEST)


class productDetail(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        
        try:
            product = Products.objects.get(pk=pk)
        except Products.DoesNotExist:
            return Response({
                        "code":"Error 404 not found",
                        "message": "Product Not Found.",
                        "data":{"status": '404'}
                        }, status=status.HTTP_404_NOT_FOUND)
            
        
        serializer = productSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        return Response({
                        "code":"authentication_error",
                        "message": "The API key provided does not have write permissions.",
                        "data":{"status": '401'}
                        }, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        return Response({
                        "code":"authentication_error",
                        "message": "The API key provided does not have write permissions.",
                        "data":{"status": '401'}
                        }, status=status.HTTP_400_BAD_REQUEST)


class categoryDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):

        try:
            category = Categories.objects.get(pk=pk)
        except Categories.DoesNotExist:
            return Response({
                        "code":"Error 404 not found",
                        "message": "Category Not Found.",
                        "data":{"status": '404'}
                        }, status=status.HTTP_404_NOT_FOUND)

        product = Products.objects.filter(category__exact=pk)
        serializer = productSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

    def post(self, request):
        return Response({
                        "code":"authentication_error",
                        "message": "The API key provided does not have write permissions.",
                        "data":{"status": '401'}
                        }, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        return Response({
                        "code":"authentication_error",
                        "message": "The API key provided does not have write permissions.",
                        "data":{"status": '401'}
                        }, status=status.HTTP_400_BAD_REQUEST)
