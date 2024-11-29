from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializer import ProductSerializer

#Product View
@api_view(['GET'])
def getProduct(request):
    products = Product.objects.all()
    Pdata = ProductSerializer(products, many=True).data
    return Response(Pdata)

@api_view(['POST'])
def createProduct(request):
    data = request.data
    sData = ProductSerializer(data=data)
    if sData.is_valid():
        sData.save()
        if sData.is_valid():
            return Response(sData.data, status=status.HTTP_201_CREATED)
        return Response(sData.errors, status=status.HTTP_400_BAD_REQUEST)
    
