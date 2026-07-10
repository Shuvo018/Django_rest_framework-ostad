from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    Published_Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title