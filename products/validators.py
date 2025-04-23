from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator
from .models import Product


def validate_title(value):
    qs = Product.objects.filter(title__iexact=value)
    if qs.exists():
        raise ValidationError(f"{value}Title already exists")
    return value


def validate_title_no_hello(value):
    if "hello" in value.lower():
        raise ValidationError(f"Hello is not allowed")
    return value


unique_product_title = UniqueValidator(queryset=Product.objects.all())
