from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL



class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,default=1)
    title = models.CharField(max_length=255)
    content = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    
    def __str__(self): 
        return self.title

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.8)

    def get_discount(self):
        return "122"