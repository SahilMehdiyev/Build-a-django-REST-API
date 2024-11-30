
from rest_framework.exceptions import ValidationError
from .models import Product

def validate_title(value):
    qs = Product.objects.filter(title__iexact=value)
    if qs.exists():
        raise ValidationError(f'{value}Title already exists')
    return value
