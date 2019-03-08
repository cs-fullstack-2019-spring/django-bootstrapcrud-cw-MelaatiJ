from django.db import models


# Create your models here.

# picture URL, name, description, and price.

class GarageSaleModel(models.Model):
    name = models.CharField(max_length=100, default="")
    description = models.TextField(max_length=500, default="")
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image_URL = models.CharField(max_length=800, default="")



    def __str__(self):
        return self.name