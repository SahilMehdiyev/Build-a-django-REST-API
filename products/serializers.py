from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            
            'title',
            'content',
            'price',
            
            # 'my_discount',  # Ensure this field is included
        ]
        
    def get_my_discount(self,obj):
        print(obj.id)
        return obj.get_discount()