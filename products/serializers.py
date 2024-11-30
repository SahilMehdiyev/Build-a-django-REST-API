from rest_framework import serializers
from .models import Product
from . import validators
from rest_framework.reverse import reverse

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name = 'product-detail',
        lookup_field = 'pk'
    )
    title = serializers.CharField(validators=[validators.validate_title_no_hello, validators.unique_product_title])
    # name = serializers.CharField(source='title', read_only=True)
    class Meta:
        model = Product
        fields = [
            'user',
            'pk',
            'url',
            'edit_url',
            # 'name',
            # 'email',
            'title',
            'content',
            'price',
            'sale_price', 
            'my_discount',  # Ensure this field is included
        ]
        
    # def validate_title(self,value):
    #     request = self.context.get('request')
    #     user = request.user
    #     qs = Product.objects.filter(user=user, title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f'{value}Title already exists')
    #     return value   
    
    # def create(self,validated_data):
    #     # return Product.objects.create(**validated_data)
    #     # email = validated_data.pop('email')
    #     # print(email)
    #     obj =  super().create(validated_data)        
    #     return obj
    
    # def update(self,instance,validated_data):
    #     email = validated_data.pop('email')
    #     return super().update(instance,validated_data)
        
        
    def get_edit_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('product-edit', kwargs={'pk': obj.pk}, request=request)
        # return f'/api/products/{obj.pk}/'
    
        
    def get_my_discount(self,obj):
        if not hasattr(obj,'id'):
            return None
        if not isinstance(obj,Product):
            return None
        return obj.get_discount()