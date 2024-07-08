from django.db import models

class Product(models.Model):
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