from django.http import Http404
from rest_framework import generics

from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_list_or_404
from.serializers import ProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_create(self,serializer):
        print(serializer.validated_data)
        
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        
        if content is None:     
            content = title
        
        serializer.save(content=content)

class ProductDetailAPIView(generics.RetrieveAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    

class ProductUpdateAPIView(generics.UpdateAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' 
    

# class ProductListAPIView(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer  
    
    
    
@api_view(['GET','POST'])
def product_alt_view(request,pk=None,  *args, **kwargs):
    method = request.method
    
    if method == 'GET':
        if pk is not None:
            #detail view
            
            obj = get_list_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        # url_args? 
        # get request -> detail
        # list view 
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
    
    if method == 'POST':
        #create an item 
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            
            title = serializer.validated_data.get['title']
            content = serializer.validated_data.get['content']or None
            
            if content is None:
                content=title
                
                
                serializer.save(content=content) 
            return Response(serializer.data)
        return Response({'invalid': 'not good data'},status=400)        
    