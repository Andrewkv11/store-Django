from django.db import models


# Create your models here.
class Product_Category(models.Model):
    name = models.CharField(max_length=30, db_index=True)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=30, db_index=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=30, db_index=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    price = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    cat = models.ForeignKey(Product_Category, on_delete=models.PROTECT, null=True)
    mnf = models.ForeignKey(Manufacturer, on_delete=models.PROTECT, null=True)
