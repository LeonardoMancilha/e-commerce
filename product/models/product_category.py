from django.db import models


class Category(models.Model):
    """
    This class is used to create a Product Category object
    """
    
    class Meta:
        verbose_name_plural = "Categories"

    category_name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    category_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    deleted_at = models.DateTimeField(null = True)

    def __str__(self):
        """
        This method returns the string representation of the object.
        """
        return self.category_name

    def get_friendly_name(self):
        """
        This method is used to return the friendly name of the category.
        """
        return self.friendly_name
    