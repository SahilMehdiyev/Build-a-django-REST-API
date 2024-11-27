from rest_framework import serializers
from .models import Product
from rest_framework import reverse

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    # url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'pk',
            # 'url',
            'title',
            'content',
            'price',
            'sale_price', 
            'my_discount',  # Ensure this field is included
        ]
        
    # def get_url(self,obj):
    #     request = self.context.get('request')
    #     return reverse('product-detail', kwargs={'pk': obj.pk}, request=request)
        # return f'/api/products/{obj.pk}/'
    
        
    def get_my_discount(self,obj):
        if not hasattr(obj,'id'):
            return None
        if not isinstance(obj,Product):
            return None
        return obj.get_discount()