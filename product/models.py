from django.db import models


# Create your models here.

# Products app with Product model.
#     Product : name, weight, price, created_at, updated_at

class productModel(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    weight = models.IntegerField(blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)
    created_at = models.TextField(blank=False, null=False)
    updated_at = models.TextField(blank=False)

    def __str__(self):
        return self.name
