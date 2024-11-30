from django.http import Http404
from rest_framework import generics,mixins,permissions,authentication
from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_list_or_404
from.serializers import ProductSerializer
from .permissions import IsStaffEditorPermission


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    ]
    permission_classes = [permissions.DjangoModelPermissions]
    
    def perform_create(self,serializer):
        # email = serializer.validated_data.pop('email')
        # print(email)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:     
            content = title
        serializer.save(content=content)  

class ProductDetailAPIView(generics.RetrieveAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    

class ProductUpdateAPIView(generics.UpdateAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' 
    
    def perform_update(self,serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


class ProductMixinView(mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       generics.GenericAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def get(self,request, *args, **kwargs):
        print(self.kwargs,self.args)
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request,*args, **kwargs)
        return self.list(request,*args, **kwargs)
    
    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self,serializer):
        print(serializer.validated_data)
        
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:     
            content = 'This is a single view'
        serializer.save(content=content)
    



    
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
    