from django.db import models


class Product(models.Model):
    """
    This class is used to create a Product object
    """
    product_name = models.CharField(max_length=254,)
    product_sku = models.CharField(max_length=254, null=True, blank=True)
    product_slug = models.SlugField(max_length=254, null=False, unique=True)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=6, decimal_places=2)
    product_image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    deleted_at = models.DateTimeField(null = True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        """
        This method returns the string representation of the object.
        """
        return self.product_name
