from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    birthday = models.DateField()
    wish_year = models.IntegerField(default=0)

    def __str__(self):
        return self.name
