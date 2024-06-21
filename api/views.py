from django.shortcuts import render
import requests
from django.http import JsonResponse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes

# Create your views here.
from rest_framework import generics
from api.models import Product
from api.serializers import ProductSerializer

def getRESTConnMetainfoEndpoint(omgeving, getconnector_naam):
    return "{}/connectors/{}".format(str('https://83607.rest.afas.online/ProfitRestServices'), getconnector_naam)

class ProductList(generics.ListCreateAPIView):
    
    
   
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = Product
    
def afas(request):
    params = dict(Authorization = "AfasToken " + 'PHRva2VuPjx2ZXJzaW9uPjE8L3ZlcnNpb24+PGRhdGE+QjBCNTg1QjJBNDNBNDAzOEE2NDUyNEZFNzc4QTFFMjdDQTIzOUY3MTQ3NDQ5N0JGQzg0QTZEQjkxM0NEODMzMjwvZGF0YT48L3Rva2VuPg==')

    
    session = requests.Session()
    getconnector = 'BI_SalesOrderLineItems?take=700000'
    


    req = requests.get(getRESTConnMetainfoEndpoint('83607', getconnector), headers=params).json()
    queryset = req['rows']
    #print(req['rows'])
    return JsonResponse(queryset, safe=False)





@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def afas_conector(request, conector=None):
    content = {
        'user': str(request.user),  # `django.contrib.auth.User` instance.
        'auth': str(request.auth),  # None
    }
    print(content)
    params = dict(Authorization = "AfasToken " + 'PHRva2VuPjx2ZXJzaW9uPjE8L3ZlcnNpb24+PGRhdGE+QjBCNTg1QjJBNDNBNDAzOEE2NDUyNEZFNzc4QTFFMjdDQTIzOUY3MTQ3NDQ5N0JGQzg0QTZEQjkxM0NEODMzMjwvZGF0YT48L3Rva2VuPg==')

    print(conector)
    session = requests.Session()
    getconnector = conector +'?take=10000'
    


    req = requests.get(getRESTConnMetainfoEndpoint('83607', getconnector), headers=params).json()
    
    #print(req['rows'])
    queryset = req['rows']
    
    return JsonResponse(queryset, safe=False)

