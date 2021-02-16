from django.db import models

class Product_item(models.Model):
    name = models.CharField(max_length=200, default='', primary_key=True)
    description = models.TextField(max_length=600,)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    TOPS = 'TP'
    COATS = 'CTS'
    JEANS = 'JNS'
    DRESSES = 'DRS'
    NEWSTOCK = 'NWK'

    Category_Clothes_Choices = [
        
        (TOPS, 'Tops'),
        (COATS, 'Coats'),
        (JEANS, 'Jeans'),
        (DRESSES, 'Dresses'),
        (NEWSTOCK, 'New Stock'),
    ]
    clothes_category = models.CharField(
        max_length=32,
        choices=Category_Clothes_Choices,
        default=TOPS,
    )
   
    #class Meta: 
      #  ordering = ['id'] 

    #def get_absolute_url(self,):
       # return reverse('products', args={self.pk})

    def __str__(self):
        return self.name

