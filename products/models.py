from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)  # Ensure this field is present
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField()
    link = models.URLField()

    def __str__(self):
        return self.name

