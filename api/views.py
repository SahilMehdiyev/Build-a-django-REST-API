from django.forms.models import model_to_dict
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


from products.models import Product
from products.serializers import ProductSerializer

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    
    """
    DRF API View
    """

    # instance = Product.objects.all().order_by('?').first()
    # data = {}
    # if instance:
    #     data = ProductSerializer(instance).data
    
    
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        instance = serializer.save()
        print(instance)
        return Response(serializer.data)
    return Response({'invalid': 'not good idea'}, status=400)
   